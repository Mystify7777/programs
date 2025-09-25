// CustomHashMap.java
public class CustomHashMap<K, V> {
    private static final int INITIAL_CAPACITY = 16;
    private static final float LOAD_FACTOR = 0.75f;

    private Entry<K,V>[] table;
    private int size;
    private int threshold;

    @SuppressWarnings("unchecked")
    public CustomHashMap() {
        table = (Entry<K,V>[]) new Entry[INITIAL_CAPACITY];
        threshold = (int)(INITIAL_CAPACITY * LOAD_FACTOR);
        size = 0;
    }

    private static class Entry<K,V> {
        final K key;
        V value;
        Entry<K,V> next;

        Entry(K key, V value, Entry<K,V> next) {
            this.key = key;
            this.value = value;
            this.next = next;
        }
    }

    private int indexFor(Object key, int length) {
        int h = (key == null) ? 0 : key.hashCode();
        // spread bits (similar to Java's)
        h ^= (h >>> 16);
        return (h & 0x7fffffff) % length;
    }

    public V get(K key) {
        int idx = indexFor(key, table.length);
        Entry<K,V> e = table[idx];
        while (e != null) {
            if (key == null ? e.key == null : key.equals(e.key))
                return e.value;
            e = e.next;
        }
        return null;
    }

    public boolean containsKey(K key) {
        return get(key) != null;
    }

    public V put(K key, V value) {
        if (size + 1 > threshold) {
            resize();
        }
        int idx = indexFor(key, table.length);
        Entry<K,V> e = table[idx];
        for (Entry<K,V> cur = e; cur != null; cur = cur.next) {
            if (key == null ? cur.key == null : key.equals(cur.key)) {
                V old = cur.value;
                cur.value = value;
                return old;
            }
        }
        // insert new head
        Entry<K,V> newEntry = new Entry<>(key, value, e);
        table[idx] = newEntry;
        size++;
        return null;
    }

    public V remove(K key) {
        int idx = indexFor(key, table.length);
        Entry<K,V> prev = null;
        Entry<K,V> cur = table[idx];
        while (cur != null) {
            if (key == null ? cur.key == null : key.equals(cur.key)) {
                if (prev == null) {
                    table[idx] = cur.next;
                } else {
                    prev.next = cur.next;
                }
                size--;
                return cur.value;
            }
            prev = cur;
            cur = cur.next;
        }
        return null;
    }

    public int size() {
        return size;
    }

    @SuppressWarnings("unchecked")
    private void resize() {
        int newCapacity = table.length * 2;
        Entry<K,V>[] newTable = (Entry<K,V>[]) new Entry[newCapacity];
        for (int i = 0; i < table.length; i++) {
            Entry<K,V> e = table[i];
            while (e != null) {
                Entry<K,V> next = e.next;
                int idx = indexFor(e.key, newCapacity);
                e.next = newTable[idx];
                newTable[idx] = e;
                e = next;
            }
        }
        table = newTable;
        threshold = (int)(newCapacity * LOAD_FACTOR);
    }

    // Simple test
    public static void main(String[] args) {
        CustomHashMap<String,Integer> map = new CustomHashMap<>();
        map.put("one", 1);
        map.put("two", 2);
        map.put("three", 3);
        System.out.println("size: " + map.size()); // 3
        System.out.println("get two: " + map.get("two")); // 2
        map.put("two", 22);
        System.out.println("get two (updated): " + map.get("two")); // 22
        System.out.println("remove one: " + map.remove("one")); // 1
        System.out.println("size after remove: " + map.size()); // 2

        // Null key test
        map.put(null, 99);
        System.out.println("null key -> " + map.get(null)); // 99
    }
}
