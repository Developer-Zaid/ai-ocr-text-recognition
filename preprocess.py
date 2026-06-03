import cv2


def preprocess_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(
            "Image not found."
        )

    # Convert to grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Resize for better OCR
    gray = cv2.resize(
        gray,
        None,
        fx=3,
        fy=3,
        interpolation=cv2.INTER_CUBIC
    )

    # Noise reduction
    gray = cv2.medianBlur(
        gray,
        3
    )

    # Strong threshold
    processed = cv2.threshold(
        gray,
        150,
        255,
        cv2.THRESH_BINARY
    )[1]

    return processed
