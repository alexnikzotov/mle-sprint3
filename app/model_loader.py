# импортируйте необходимую библиотеку
from catboost import CatBoostClassifier
# ваш код здесь

def load_churn_model(model_path: str):
    """Загружаем обученную модель оттока.
    Args:
        model_path (str): Путь до модели.
    """
    try:
        # ваш код здесь — загрузите модель
        model = CatBoostClassifier() #.load_model()
        model.load_model(model_path)
        print("Model loaded successfully")
        return model
    except Exception as e:
        print(f"Failed to load model: {e}")
        return None

if __name__ == "__main__":
    # вызовите функцию load_churn_model с нужным путём
    # ваш код здесь  
    # выведите параметры модели через print(f"Model parameter names: {}") 
    # ваш код здесь 
    model = load_churn_model(model_path='models/catboost_churn_model.bin')
    model_path = "path/to/your/model"
    loaded_model = load_churn_model(model_path)
    if loaded_model:
        print(f'Model parameter names: {model.feature_names_}')