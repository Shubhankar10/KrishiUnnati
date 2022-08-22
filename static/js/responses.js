function getBotResponse(input) {

    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    }
    else if (input == "Hi") {
        return "Hello User!";
    }
    else if (input == "Tell me something about farming") {
        return "Agriculture is the largest employer in the world";
    }
    else if (input == "Why should we prefer your Website?") {
        return "Cause we have made it easy for you to interact with us!";
    }
    else if (input == "Who made you?") {
        return "My Masters, Shubhankar, Akshat, Sanskar, Shreoshi, Disha and Yash are the creators of this website!";
    }
    else if (input == "Which state has the highest agricultural produce?") {
        return "Uttar Pradesh";
    }
    else if (input == "Can you help me to identify and diagnose the plant disease?") {
        return "Yes, we can help you to identify and diagnose the plant disease!";
    }
    else if (input == "Why should we prefer your Website?") {
        return "Cause we have made it easy for you to interact with us";
    }
    else if (input == "Why should we prefer your Website?") {
        return "Cause we have made it easy for you to interact with us";
    }else {
        return "Try asking something else!";
    }
}