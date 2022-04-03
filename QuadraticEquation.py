# %%
EPS = 1e-6


class ParamAZeroError(Exception):
    pass


class ConvertToFloatError(Exception):
    pass


class QuadraticEquation:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def solve(self) -> list:
        try:
            a = float(self.a)
            b = float(self.b)
            c = float(self.c)
        except:
            raise ConvertToFloatError

        discr = b**2 - 4 * a * c

        if abs(a) < EPS:
            raise ParamAZeroError

        roots = []
        if discr > EPS:
            root0 = (-b + (discr) ** 0.5) / (2 * a)
            root1 = (-b - (discr) ** 0.5) / (2 * a)
            roots.append(min(root0, root1))
            roots.append(max(root0, root1))
        elif abs(discr) < EPS:
            root = -b / (2 * a)
            roots.append(root)

        return roots


if __name__ == "__main__":
    equation = QuadraticEquation(1, 2, 1.0000001)
    roots = equation.solve()
    print(f"Roots: {roots}")
