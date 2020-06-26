package application;

import java.util.Iterator;

public class CircularlyListDeque<E> implements Deque<E> {
    private CircularlyLinkedList<E> list;
    
    public CircularlyListDeque() {
        list = new CircularlyLinkedList<E>();
    }
    //TODO: implement all methods of Deque<E>
    
    private static void onFalseThrow(boolean b) {
        if(!b)
            throw new RuntimeException("Error: unexpected");            
    }
    
    @SuppressWarnings("unused")
    public static void main(String[] args) {
        CircularlyListDeque<Integer> dq = new CircularlyListDeque<Integer>();

        for(int i : dq)
            onFalseThrow(false);
        onFalseThrow(dq.size() == 0);
        onFalseThrow(dq.isEmpty() == true);
        
        dq.addFirst(3);
        dq.addFirst(2);
        dq.addFirst(1);
        dq.addLast(4);
        dq.addLast(5);
        
        int j = 1;
        for(int i : dq)
            onFalseThrow(i == j++);
        onFalseThrow(dq.size() == 5);
        onFalseThrow(dq.isEmpty() == false);

        for(int i = 1; i <= 3; i++)
            onFalseThrow(i == dq.removeFirst());
        onFalseThrow(dq.removeLast() == 5);
        onFalseThrow(dq.removeLast() == 4);
        
        onFalseThrow(dq.size() == 0);
        onFalseThrow(dq.isEmpty() == true);
        
        System.out.println("Success!");        
    }    
}
