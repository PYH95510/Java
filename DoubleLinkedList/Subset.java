package hw214_3;

//a = Subset({1,2}, {1,2,3,4}), b = Subset({2,3}, {1,2,3,4});
//a and b = Subset({2},     {1,2,3,4})
//a or  b = Subset({1,2,3}, {1,2,3,4})
//not a   = Subset({3,4},   {1,2,3,4})

public class Subset<E extends Comparable<E>> implements BooleanAlgebra {
    private Set<E> subset;
    private Set<E> univ;
    
    public Subset(Set<E> subset, Set<E> univ) {
        this.subset = subset.union(new SetImpl<E>());
        this.univ = univ.union(new SetImpl<E>());
    }
    
    //interface BooleanAlgebra
    public BooleanAlgebra or(BooleanAlgebra a) {
        //TODO: return the union as a Subset
    }
    public BooleanAlgebra and(BooleanAlgebra a) {
        //TODO: return the intersection as a Subset
    }
    public BooleanAlgebra not() {
        //TODO: return univ - subset as a Subset
    }
    public BooleanAlgebra orIdentity() {
        //TODO: return the empty set as a Subset
    }
    public BooleanAlgebra andIdentity() {
        //TODO: return univ as a Subset
    }
    public boolean isEqual(BooleanAlgebra a) {
        Subset<E> s = castOrThrow(a);
        return subset.isEqual(s.subset) && univ.isEqual(s.univ);
    }

    @SuppressWarnings("unchecked")
    private Subset<E> castOrThrow(BooleanAlgebra a) {
        Subset<E> s = (Subset<E>)a;
        if(!univ.isEqual(s.univ))
            throw new IllegalArgumentException("Unmatched univere");
        return s;
    }
}
