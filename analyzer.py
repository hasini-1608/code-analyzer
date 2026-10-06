import ast


def analyze_code(code):
    try:
        tree = ast.parse(code)

        issues = []

        # Check for missing docstrings
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                if ast.get_docstring(node) is None:
                    issues.append(
                        f"Missing docstring in {node.name}"
                    )

        # Check for bare except
        for node in ast.walk(tree):
            if isinstance(node, ast.ExceptHandler):
                if node.type is None:
                    issues.append("Bare except detected")

        if not issues:
            issues.append("No major issues found.")

        return {
            "success": True,
            "message": "Code analyzed successfully.",
            "issues": issues
        }

    except SyntaxError as error:
        return {
            "success": False,
            "message": f"Syntax error on line {error.lineno}: {error.msg}",
            "issues": []
        }