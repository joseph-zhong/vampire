from environments.random_search import RandomSearch
from environments.datasets import DATASETS
import os


CLASSIFIER = {
        "LAZY_DATASET_READER": 0,
        "CUDA_DEVICE": 0,
        "EVALUATE_ON_TEST": 0,
        "NUM_EPOCHS": 50,
        "SEED": 93408,
        "SEQUENCE_LENGTH": 400,
        "TRAIN_PATH": os.environ["DATA_DIR"] + "/train.jsonl",
        "DEV_PATH":  os.environ["DATA_DIR"] + "/dev.jsonl",
        "TEST_PATH":  os.environ["DATA_DIR"] + "/test.jsonl",
        "THROTTLE": os.environ.get("THROTTLE", None),
        "USE_SPACY_TOKENIZER": 1,
        "FREEZE_EMBEDDINGS": ["VAMPIRE"],
        "EMBEDDINGS": ["VAMPIRE", "RANDOM"],
        "ENCODER": "AVERAGE",
        "EMBEDDING_DROPOUT": 0.5,
        "LEARNING_RATE": 0.004,
        "DROPOUT": 0.5,
        "VAMPIRE_DIRECTORY": os.environ.get("VAMPIRE_DIR", None),
        "VAMPIRE_DIM": os.environ.get("VAMPIRE_DIM", None),
        "BATCH_SIZE": 32,
        "NUM_ENCODER_LAYERS": 1,
        "NUM_OUTPUT_LAYERS": 2, 
        "MAX_FILTER_SIZE": RandomSearch.random_integer(3, 6),
        "NUM_FILTERS": RandomSearch.random_integer(64, 512),
        "HIDDEN_SIZE": RandomSearch.random_integer(64, 512),
        "AGGREGATIONS": RandomSearch.random_subset("maxpool", "meanpool", "attention", "final_state"),
        "MAX_CHARACTER_FILTER_SIZE": RandomSearch.random_integer(3, 6),
        "NUM_CHARACTER_FILTERS": RandomSearch.random_integer(16, 64),
        "CHARACTER_HIDDEN_SIZE": RandomSearch.random_integer(16, 128),
        "CHARACTER_EMBEDDING_DIM": RandomSearch.random_integer(16, 64),
        "CHARACTER_ENCODER": RandomSearch.random_choice("LSTM", "CNN", "AVERAGE"),
        "NUM_CHARACTER_ENCODER_LAYERS": RandomSearch.random_choice(1, 2),
}

VAMPIRE = {
        "LAZY_DATASET_READER": 0,
        "KL_ANNEALING": "linear",
        "SIGMOID_WEIGHT_1": 0.25,
        "SIGMOID_WEIGHT_2": 15,
        "LINEAR_SCALING": 1000,
        "VAE_HIDDEN_DIM":  81,
        "ADDITIONAL_UNLABELED_DATA_PATH": None,
        "TRAIN_PATH": os.environ["DATA_DIR"] + "/train.npz",
        "DEV_PATH": os.environ["DATA_DIR"] + "/dev.npz",
        "REFERENCE_COUNTS": os.environ["DATA_DIR"] + "/reference/ref.npz",
        "REFERENCE_VOCAB": os.environ["DATA_DIR"] + "/reference/ref.vocab.json",
        "VOCABULARY_DIRECTORY": os.environ["DATA_DIR"] + "/vocabulary/",
        "NUM_ENCODER_LAYERS": 2,
        "ENCODER_ACTIVATION": "relu",
        "MEAN_PROJECTION_ACTIVATION": "linear",
        "NUM_MEAN_PROJECTION_LAYERS": 1,
        "LOG_VAR_PROJECTION_ACTIVATION": "linear",
        "NUM_LOG_VAR_PROJECTION_LAYERS": 1,
        "SEED": 34543,
        "Z_DROPOUT": 0.49,
        "LEARNING_RATE": 0.00021,
        "TRACK_NPMI": True,
        "CUDA_DEVICE": 0,
        "UPDATE_BACKGROUND_FREQUENCY": 0,
        "VOCAB_SIZE": 30000,
        "APPLY_BATCHNORM": 1,
        "APPLY_BATCHNORM_1": 0,
        "BATCH_SIZE": 64,
        "VALIDATION_METRIC": "+npmi"
}



ENVIRONMENTS = {
        'VAMPIRE': VAMPIRE,
        "CLASSIFIER": CLASSIFIER,
}






