def describe_model(name: str, score: float) -> str:
    return f"{name} has a score of {score:.3f}"

def main():
    model_name = "AlexNet"
    example_score = 0.65
    result = describe_model(model_name, example_score)
    print(result)


if __name__ == "__main__":
    main()
