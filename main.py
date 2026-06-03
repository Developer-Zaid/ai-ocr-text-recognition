import cv2
import pytesseract

from preprocess import preprocess_image


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text(image_path):

    processed = preprocess_image(
        image_path
    )

    text = pytesseract.image_to_string(
        processed
    )

    cv2.imwrite(
        "output/processed_image.png",
        processed
    )

    return text


def main():

    print("=" * 60)
    print("OCR TEXT RECOGNITION SYSTEM")
    print("=" * 60)

    filename = input(
        "\nEnter image filename: "
    )

    image_path = (
        f"sample_images/{filename}"
    )

    try:

        text = extract_text(
            image_path
        )

        print("\nDetected Text:\n")

        print(text)

    except Exception as error:

        print(
            f"\nError: {error}"
        )


if __name__ == "__main__":
    main()
