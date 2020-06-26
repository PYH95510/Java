package HW4;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.jupiter.api.Test;

public class MergeSortTest {

	@Test
	public void wellSortedArrayShouldReturnTrue() {

		assertTrue(MergeSort.sorted(new int[] {2,33,45,90,200}));
		assertTrue(MergeSort.sorted(new int[] {}));
		assertFalse(MergeSort.sorted(new int[] {4,3,1,2}));
		assertFalse(MergeSort.sorted(new int[] { 1, 3, 7, 8, 9, 10, 0 }));

	}

}
