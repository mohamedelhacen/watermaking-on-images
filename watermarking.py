import cv2

image_path = input("Enter the path to the image: ")
watermark_path = input("Enter the path to the watermark: ")

image = cv2.imread(image_path)
watermark = cv2.imread(watermark_path)

image_width, image_height = image.shape[0], image.shape[1]
watermark = cv2.resize(watermark, (int(image_width/10), int(image_height/10)))

rows, cols = watermark.shape[0], watermark.shape[1]
roi = image[image_width - rows:image_width, image_height - cols:image_height]

watermark_gray = cv2.cvtColor(watermark, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(watermark_gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
fg = cv2.bitwise_and(watermark, watermark, mask=mask)

dst = cv2.add(fg, bg)
image[image_width - rows:image_width, image_height - cols:image_height] = dst

cv2.imshow("Watermarked", image)
if cv2.waitKey() & ord('s'):
    cv2.imwrite("output.jpg", image)
cv2.destroyAllWindows()