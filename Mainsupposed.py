from utils.PredictGrade import load_student_data, train_model, predict_grade



X, y = load_student_data()
model = train_model(X, y)
predict_grade(model)