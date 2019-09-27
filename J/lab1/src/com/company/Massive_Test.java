//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package com.company;

class Massiv_Test {
    private long[] a;
    private int nElems;

    public Massiv_Test(int max) {
        this.a = new long[max];
        this.nElems = 0;
    }

    public boolean find(long searchKey) {
        int j;
        for(j = 0; j < this.nElems && this.a[j] != searchKey; ++j) {
        }

        return j != this.nElems;
    }

    public void insert(long value) {
        this.a[this.nElems] = value;
        ++this.nElems;
    }

    public boolean delete(long value) {
        int j;
        for(j = 0; j < this.nElems && value != this.a[j]; ++j) {
        }

        if (j == this.nElems) {
            return false;
        } else {
            for(int k = j; k < this.nElems; ++k) {
                this.a[k] = this.a[k + 1];
                --this.nElems;
            }

            return true;
        }
    }

    public void display() {
        for(int j = 0; j < this.nElems; ++j) {
            System.out.print(this.a[j]);
        }

        System.out.println("");
    }
}
