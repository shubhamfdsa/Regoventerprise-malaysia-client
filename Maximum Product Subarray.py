def evalRPN(tokens):
    stack = []

    # Iterate through the tokens
    for token in tokens:
        # If the token is an operator, pop the last two operands and perform the operation
        if token in ["+", "-", "*", "/"]:
            op2 = stack.pop()
            op1 = stack.pop()

            if token == "+":
                result = op1 + op2
            elif token == "-":
                result = op1 - op2
            elif token == "*":
                result = op1 * op2
            else:
                # Note that the division between two integers always truncates toward zero
                result = int(op1 / op2)

            # Push the result onto the stack
            stack.append(result)
        else:
            # If the token is an operand, push it onto the stack
            stack.append(int(token))

    # The final result is the only element remaining in the stack
    return stack[0]


def maxProduct(nums):
    # Initialize the maximum and minimum products
    max_product = nums[0]
    min_product = nums[0]

    # Initialize the overall maximum product
    overall_max = nums[0]

    # Iterate through the array
    for i in range(1, len(nums)):
        # Calculate the new maximum and minimum products
        temp_max = max(nums[i], max_product * nums[i], min_product * nums[i])
        temp_min = min(nums[i], max_product * nums[i], min_product * nums[i])

        # Update the overall maximum product
        overall_max = max(overall_max, temp_max)

        # Update the maximum and minimum products
        max_product = temp_max
        min_product = temp_min

    return overall_max
tokens = ["4","2","+","5","*"]
print(evalRPN(tokens)) # Output: 30
nums = [2,3,-2,4]
print(maxProduct(nums))

