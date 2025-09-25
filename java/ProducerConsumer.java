// ProducerConsumer.java
public class ProducerConsumer {
    static class BoundedBuffer {
        private final int[] buffer;
        private int putPtr = 0, takePtr = 0, count = 0;

        public BoundedBuffer(int capacity) {
            buffer = new int[capacity];
        }

        public synchronized void put(int x) throws InterruptedException {
            while (count == buffer.length) {
                wait();
            }
            buffer[putPtr] = x;
            putPtr = (putPtr + 1) % buffer.length;
            count++;
            notifyAll();
        }

        public synchronized int take() throws InterruptedException {
            while (count == 0) {
                wait();
            }
            int val = buffer[takePtr];
            takePtr = (takePtr + 1) % buffer.length;
            count--;
            notifyAll();
            return val;
        }
    }

    static class Producer implements Runnable {
        private final BoundedBuffer buf;
        private final int id;
        private final int produceCount;
        Producer(BoundedBuffer b, int id, int produceCount) { buf = b; this.id = id; this.produceCount = produceCount; }
        public void run() {
            try {
                for (int i = 0; i < produceCount; i++) {
                    int item = id * 1000 + i;
                    buf.put(item);
                    System.out.println("Producer " + id + " produced " + item);
                    Thread.sleep((long)(Math.random() * 200));
                }
            } catch (InterruptedException ignored) {}
        }
    }

    static class Consumer implements Runnable {
        private final BoundedBuffer buf;
        private final int id;
        private final int consumeCount;
        Consumer(BoundedBuffer b, int id, int consumeCount) { buf = b; this.id = id; this.consumeCount = consumeCount; }
        public void run() {
            try {
                for (int i = 0; i < consumeCount; i++) {
                    int item = buf.take();
                    System.out.println("Consumer " + id + " consumed " + item);
                    Thread.sleep((long)(Math.random() * 300));
                }
            } catch (InterruptedException ignored) {}
        }
    }

    public static void main(String[] args) throws InterruptedException {
        BoundedBuffer buffer = new BoundedBuffer(5);
        Thread p1 = new Thread(new Producer(buffer, 1, 10));
        Thread p2 = new Thread(new Producer(buffer, 2, 10));
        Thread c1 = new Thread(new Consumer(buffer, 1, 10));
        Thread c2 = new Thread(new Consumer(buffer, 2, 10));

        p1.start(); p2.start(); c1.start(); c2.start();

        p1.join(); p2.join();
        c1.join(); c2.join();
        System.out.println("All done.");
    }
}
