import java.util.List;

public class Rectangle extends Quadrilateral implements SymmetricTwoDShape {

    /**
     * The center of a rectangle is calculated to be the point of intersection of its diagonals.
     *
     * @return the center of this rectangle.
     */
    @Override
    public Point center() {
        return null; // TODO
    }

    @Override
    public boolean isMember(List<? extends Point> vertices) {
        return false; // TODO
    }

    @Override
    public double area() {
        return 0d; // TODO
    }
}
