import tensorflow as tf
import tensorflow_hub as hub

module_handle = "https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1"


def to_tensor(pil_img):
    converted = tf.image.convert_image_dtype(
        pil_img,
        tf.float32
    )[tf.newaxis, ...]

    return converted


def perform_od(im_tensor):
    detector = hub.load(module_handle).signatures['default']
    results = detector(im_tensor)
    results = {key: value.numpy() for key, value in results.items()}

    classes = list(map(
        lambda x: x.decode('utf-8'),
        results['detection_class_entities']
    ))

    results = dict(
        zip(classes, results['detection_scores'])
    )

    results = dict(
        sorted(results.items(), key=lambda x: x[1], reverse=True)
    )

    return results
