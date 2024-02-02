from PIL import Image
import numpy as np
import os


def reduce_colors(image_path, num_colors):
    img = Image.open(image_path)

    img_rgb = img.convert('RGB')

    pixels = np.array(img_rgb).reshape((-1, 3))
    _, labels, centers = kmeans(pixels, num_colors)

    # Replace each pixel with its corresponding center color
    quantized_pixels = centers[labels].reshape(img_rgb.size[1], img_rgb.size[0], 3)
    quantized_img = Image.fromarray(np.uint8(quantized_pixels))
    quantized_img.save('reduced_base.png')
    return quantized_img, labels, centers


def kmeans(pixels, k, max_iters=100):
    centers = pixels[np.random.choice(range(len(pixels)), k, replace=False)]

    for _ in range(max_iters):
        labels = np.argmin(np.linalg.norm(pixels[:, np.newaxis] - centers, axis=2), axis=1)

        new_centers = np.array([pixels[labels == i].mean(axis=0) if np.any(labels == i) else centers[i] for i in range(k)])

        if np.all(centers == new_centers):
            break

        centers = new_centers

    return centers, labels, new_centers



def save_individual_colors(image, labels, centers, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    image_array = np.array(image)
    unique_labels, _ = np.unique(labels, return_counts=True)

    for label in unique_labels:
        single_color_pixels = np.zeros_like(image_array)
        single_color_pixels[labels.reshape(image_array.shape[:2]) == label] = centers[label]
        single_color_img = Image.fromarray(np.uint8(single_color_pixels))
        
        hex_color = "#{:02x}{:02x}{:02x}".format(*map(int, centers[label]))

        output_path = os.path.join(output_folder, f'color_{hex_color}.png')

        single_color_img.save(output_path)



if __name__ == "__main__":
    input_image_path = str(input("Image's name to split: "))
    num_colors = int(input("Enter the number of colors: "))
    output_folder = str(input("Output folder: "))

    reduced_image, color_labels, color_centers = reduce_colors(input_image_path, num_colors)
    
    save_individual_colors(reduced_image, color_labels, color_centers, output_folder)

    print('ok')
