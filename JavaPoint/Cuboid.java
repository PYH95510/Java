import java.util.List;

// TODO : a missing interface method must be implemented in this class to make it compile. This must be in terms of volume().
public class Cuboid implements ThreeDShape {

    private final ThreeDPoint[] vertices = new ThreeDPoint[8];

    /**
     * Creates a cuboid out of the list of vertices. It is expected that the vertices are provided in
     * the order as shown in the figure given in the homework document (from v0 to v7).
     * 
     * @param vertices the specified list of vertices in three-dimensional space.
     */
    public Cuboid(List<ThreeDPoint> vertices) {
        if (vertices.size() != 8)
            throw new IllegalArgumentException(String.format("Invalid set of vertices specified for %s",
                                                             this.getClass().getName()));
        int n = 0;
        for (ThreeDPoint p : vertices) this.vertices[n++] = p;
    }

    @Override
    public double volume() {
        return 0; // TODO
    }

    @Override
    public ThreeDPoint center() {
        return null; // TODO
    }

}
