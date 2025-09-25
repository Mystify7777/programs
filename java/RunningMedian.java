// RunningMedian.java
import java.util.PriorityQueue;
import java.util.Collections;

public class RunningMedian {
    private PriorityQueue<Integer> low; // max-heap
    private PriorityQueue<Integer> high; // min-heap

    public RunningMedian() {
        low = new PriorityQueue<>(Collections.reverseOrder());
        high = new PriorityQueue<>();
    }

    public void add(int num) {
        if (low.isEmpty() || num <= low.peek()) {
            low.add(num);
        } else {
            high.add(num);
        }
        // rebalance
        if (low.size() > high.size() + 1) {
            high.add(low.poll());
        } else if (high.size() > low.size() + 1) {
            low.add(high.poll());
        }
    }

    public double getMedian() {
        if (low.size() == high.size()) {
            if (low.isEmpty()) return 0;
            return (low.peek() + high.peek()) / 2.0;
        } else if (low.size() > high.size()) {
            return low.peek();
        } else {
            return high.peek();
        }
    }

    public static void main(String[] args) {
        RunningMedian rm = new RunningMedian();
        int[] stream = {5, 15, 1, 3, 8, 7, 9};
        for (int x : stream) {
            rm.add(x);
            System.out.println("Added " + x + " -> median = " + rm.getMedian());
        }
    }
}
