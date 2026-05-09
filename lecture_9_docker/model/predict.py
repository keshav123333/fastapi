import pandas as pd
 
import pickle


# Lazy-load model to avoid import-time failures
MODEL_VERSION = "1.0"
_model = None

def get_model():
    global _model
    if _model is None:
        try:
            with open("model.pkl","rb") as f:
                _model=pickle.load(f)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to load model: {str(e)}")
    return _model


def predict_risk(data):
    model=get_model()
    prediction = model.predict(data)[0]
    predictionclass=model.predict_proba(data)[0]
    classes=model.classes_
    prediction_dict={classes[i]:predictionclass[i] for i in range(len(classes))}
    max_class={"max":max(predictionclass)}

    return {'predicted_category': prediction, 'prediction_probabilities': prediction_dict, 'max_probability': max_class}
