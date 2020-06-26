from .quadrilateral import Quadrilateral


class ShapeSorter:
    class ShapeSorter:
        def sort(*args):
            shapelis = []
            for i in args:
                if isinstance(i, Quadrilateral):
                    shapelis.append(i)

            return sorted(shapelis, key=lambda shape: shape.smallest_x())
