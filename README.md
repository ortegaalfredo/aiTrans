# aiTrans
Multi-language transpiler (source-to-source compiler) using AI

# Description
aiTrans is a transpiler that utilizes artificial intelligence (AI) to convert code written in one programming language to another. The purpose of this project is to make it easier for developers to switch between programming languages without having to manually rewrite their code. The source code can be plain english, and the transpiler will output code in the any language. The default AI is ChatGPT 3.5 and it supports most popular languages like C, C++, python, rust, etc.

# Features
The AI-based transpiler has several features, including:

* Language Translation: The transpiler can convert code written in one programming language to another. For example, it can convert Python code to JavaScript code.

* Speed: The transpiler can quickly translate code, making it ideal for use in development environments where time is of the essence.

* Customizability: The transpiler can be customized to suit the specific needs of developers. For example, developers can specify which programming languages they want to translate code between.

* Flexibility: You can instruct the AI to change the language of the comments, or to rewrite the code in the same language but obfuscated, or the same language but with a backdoor on it.

# Installation
To install the AI-based transpiler, follow these steps:

1. Clone the repository.
2. Get an API key from OpenAI and place it in api-key.txt
3. Run it with:

    ./aiTrans -h

# Usage

    aiTrans.py [-h] -s SOURCE [-l LANGUAGE] [-a]

* Parameter -s indicates the source code
* Parameter -l indicates the target language
* Parameter -a indicates the AI to read the whole source instead of line-by-line. Usually, whole source is better, but you can switch to line-by-line processing if the source code is too big to fit in the AI context. Line-by-line is currently only tested on python as a target language.

# Example

The file example2.ai is:

    print a message welcoming the user to the example script #2
    Write code to parse arguments. If the argument is "-a" variable 'A' is true.
    If the variable 'A' is true then write the message "Turbo activated", else write "Too bad, turbo deactivated"


An example conversion to python (default language) could be:

    ./aiTrans.py -s example2.ai -a > example2.python

Output would be:

    # print a message welcoming the user to the example script #2
    print("Welcome to Example Script #2")
    
    import argparse
    
    # create an ArgumentParser object
    parser = argparse.ArgumentParser()
    
    # add the argument -a
    parser.add_argument("-a", action="store_true")
    
    # parse the arguments
    args = parser.parse_args()
    
    # check if the argument -a was passed
    if args.a:
        # if the argument -a was passed, print "Turbo activated"
        print("Turbo activated")
    else:
        # if the argument -a was not passed, print "Too bad, turbo   deactivated"
        print("Too bad, turbo deactivated")


To convert the English description to C instead, the command would be:

    ./aiTrans.py -s example2.ai -a -l C > example2.c

Output would be:

    #include <stdio.h>
    
    int main(int argc, char *argv[]) {
        printf("Welcome to Example Script #2!\n"); // print welcome message
        
        int A = 0; // initialize variable A to false
        
        // loop through arguments
        for (int i = 1; i < argc; i++) {
            if (strcmp(argv[i], "-a") == 0) { // if argument is "-a"
                A = 1; // set variable A to true
            }
        }
        
        if (A) { // if variable A is true
            printf("Turbo activated\n"); // print message
        } else {
            printf("Too bad, turbo deactivated\n"); // print message
        }
        
        return 0;
    }
    


To convert the English description to rust instead, the command would be:

    ./aiTrans -s example2.ai -a -l "rust" > example2.rs

Output:

    fn main(){ // main function
        println!("Welcome to Example Script #2!"); // print welcome message
        let mut A = false; // initialize variable A as false
        for arg in std::env::args().skip(1){ // loop through command line arguments
            if arg == "-a"{ // if argument is "-a"
                A = true; // set variable A to true
            }
        }
        if A { // if variable A is true
            println!("Turbo activated"); // print "Turbo activated"
        } else { // if variable A is false
            println!("Too bad, turbo deactivated"); // print "Too bad, turbo deactivated"
        }
    }
    

# Technologies Used
The transpiler source code is developed using plain English in aiTrans.ai and openaiConnector.ai. This source code is then transpiled to the final implementation in python by writing:

    make boot
Then the transpiler can compile itself using the command:

    make

# Errors

Depending on the AI accuracy, and the vagueness of the source description, the output code might have some errors. You can generally improve the description to make it more specific and avoid most errors.

# Contributing
If you would like to contribute to the AI-based transpiler project, please follow these steps:

Fork the repository.
Make your changes.
Submit a pull request.

# License
This project is licensed under the BSD 2-clause License.
