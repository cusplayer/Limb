//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package com.company;

public class Main {
    public Main() {
    }

    public static void main(String[] args) {
        Massiv_Test Test = new Massiv_Test(15);

        for(int i = 0; i < 15; ++i) {
            Test.insert((long)i);
        }

        Test.display();
        if (Test.find(10)) {
            System.out.println("Элемент есть в массиве");
        } else {
            System.out.println("Элемента нет в массиве");
        }

        if (Test.delete(10)) {
            System.out.println("Элемент удален");
        } else {
            System.out.println("Элемента не найден");
        }

        Test.display();
    }
}

