import argparse
import tensorflow as tf

def evaluate_model(test_dir, model_dir, batch_size):
    # Load the test data
    test_dataset = tf.keras.preprocessing.image_dataset_from_directory(
        test_dir,
        batch_size=batch_size,
        image_size=(224, 224),
        label_mode='categorical'
    )

    # Load the trained model
    model = tf.keras.models.load_model(model_dir)

    # Evaluate the model
    test_loss, test_acc = model.evaluate(test_dataset)
    print(f'Test Loss: {test_loss}, Test Accuracy: {test_acc}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_dir', type=str, required=True)
    parser.add_argument('--model_dir', type=str, required=True)
    parser.add_argument('--batch_size', type=int, default=32)

    args = parser.parse_args()

    evaluate_model(args.test_dir, args.model_dir, args.batch_size)