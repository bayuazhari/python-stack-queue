# Python: Stack dan Queue

## Konsep Dasar Stack

- **Definisi dan karakteristik:** stack adalah struktur data linear yang dapat menambahkan dan menghapus elemen hanya pada satu ujung (disebut top).
- **Prinsip kerja:** elemen terakhir yang dimasukkan ke dalam stack akan menjadi elemen pertama yang dihapus, atau yang dikenal dengan istilah LIFO (Last-In-First-Out).
- **Operasi stack:** terdapat dua operasi utama dalam stack, yaitu push (menambahkan elemen ke top) dan pop (menghapus elemen dari top).
- **Implementasi stack:** stack dapat diimplementasikan menggunakan array atau linked list.

## Manipulasi Stack dengan Python

1. Membuat stack dengan Python menggunakan list

~~~
stack = []
~~~

2. Menambahkan elemen ke dalam stack menggunakan metode `append`

~~~
stack.append(elemen)
~~~

3. Menghapus elemen dari top stack menggunakan metode `pop`

~~~
stack.pop()
~~~

4. Melihat elemen yang berada pada top stack menggunakan indeks -1

~~~
stack[-1]
~~~

## Konsep Dasar Queue

- **Definisi dan karakteristik:** queue adalah struktur data linear yang mirip dengan stack, namun memungkinkan penyisipan elemen hanya pada satu ujung (disebut rear) dan penghapusan elemen hanya pada ujung yang lain (disebut front).
- **Prinsip kerja:** elemen pertama yang dimasukkan ke dalam queue akan menjadi elemen yang pertama pula dihapus, atau yang dikenal dengan istilah FIFO (First-In-First-Out).
- **Operasi queue:** terdapat dua operasi utama dalam queue, yaitu enqueue (menambahkan elemen ke rear) dan dequeue (menghapus elemen dari front).
- **Implementasi queue:** queue dapat diimplementasikan menggunakan array atau linked list.

## Manipulasi Queue dengan Python

1. Membuat queue dengan Python menggunakan deque dari modul collections

~~~
from collections import deque
queue = deque()
~~~

2. Menambahkan elemen ke dalam queue menggunakan metode `append`

~~~
queue.append(elemen)
~~~

3. Menghapus elemen dari front queue menggunakan metode `popleft`

~~~
queue.popleft()
~~~

4. Melihat elemen yang berada pada front queue menggunakan indeks 0

~~~
queue[0]
~~~