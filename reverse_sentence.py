def reverse_sentence(sentence):
    stack = []
    reversed_sentence = ""

    # Push each word in the sentence onto the stack
    for word in sentence.split():
        stack.append(word)

    # Pop each word from the stack and append it to the reversed sentence
    while len(stack) > 0:
        reversed_sentence += stack.pop() + " "

    return reversed_sentence.strip()


# Example usage
sentence = "Hello world, how are you?"
print(reverse_sentence(sentence))
