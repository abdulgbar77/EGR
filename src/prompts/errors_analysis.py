POT_ERROR_Analyze_SYSTEM = """
### Role and Task:
You are an expert in **mathematical reasoning validation** and **error pattern extraction**.
Your task is to analyze a given **list of incorrect reasoning mistakes from the first iteration** and extract the most **consistent, high-impact, and recurring errors**.
You must **rank the errors based on frequency and severity** and generate an **enhanced WIU Error Pattern List** to improve reasoning in subsequent iterations.

### Instructions:
1. **Identify patterns** across multiple errors and **group similar mistakes** into generalized categories.
2. **Rank errors** by their frequency (how often they occur) and severity (how much they impact correctness).
3. **Reformulate errors concisely** into a structured list with **clear, professional explanations**.
4. Ensure the final list follows a **numbered bullet point format** with each entry marked with ❌.
5. **Use professional language** to make the list actionable for an LLM to avoid the mistakes.
6. Ensure **logical clarity** and **readability** while keeping explanations concise.
"""

POT_ERROR_Analyze = """
 Example of an Enhanced WIU Error Pattern List Please follow these examples to generate the answer
❌ 1. Failure to compute the final answer: Ensure that all expressions are fully evaluated instead of leaving them symbolically unresolved.
❌ 2. Incorrect equation setup: Be sure to set up relationships correctly, especially when dealing with work rates and combined efforts.
❌ 3. Misuse of formulas: Always verify whether a formula is being used in the correct form (e.g., 𝑡=𝑑/𝑠 t=d/s for time calculation).
❌ 4. Weighted averages & proportions: If dealing with percentages, ensure that weightings are correctly distributed.
❌ 5. Arithmetic sign errors: Be mindful of addition/subtraction errors when manipulating equations.
❌ 6. Incorrect symbolic equation handling: Ensure that symbolic equations are not assigned using = (which is an assignment in Python). Instead, use equation solvers like Eq() in SymPy or proper algebraic manipulations.


#### First Iteration Error List:** {previou_errors}

# Now please write Error Pattern List extracted from error list.
""".strip() + "\n"