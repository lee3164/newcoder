package data_structure

import (
	"testing"
)

var (
	comparator = func(x, y interface{}) int {
		ix := x.(int)
		iy := y.(int)
		if ix < iy {
			return -1
		} else if ix > iy {
			return 1
		} else {
			return 0
		}
	}
)

func TestSkipList_Insert(t *testing.T) {
	skipList := NewSkipList(comparator)
	for i := 0; i < 100; i++ {
		skipList.Insert(i)
	}
	skipList.Print()
}

func TestSkipList_Delete(t *testing.T) {
	skipList := NewSkipList(comparator)
	for i := 0; i < 100; i++ {
		skipList.Insert(i)
	}
	if skipList.Delete(10) != true {
		t.FailNow()
	}
	if skipList.Delete(10) != false {
		t.FailNow()
	}
	if skipList.Delete(101) != false {
		t.FailNow()
	}
	skipList.Print()
}

func TestSkipListIter_Next(t *testing.T) {
	skipList := NewSkipList(comparator)
	for i := 0; i < 100; i++ {
		skipList.Insert(i)
	}
	iter := skipList.Iterator()
	if !iter.Next() {
		t.FailNow()
	}

	skipList = NewSkipList(comparator)
	iter = skipList.Iterator()
	if iter.Next() {
		t.FailNow()
	}
}

func TestSkipListIter_At(t *testing.T) {
	skipList := NewSkipList(comparator)
	for i := 0; i < 100; i++ {
		skipList.Insert(i)
	}
	iter := skipList.Iterator()
	for i := 0; i < 100; i++ {
		if iter.Next() {
			v, err := iter.At()
			if err != nil {
				t.Error(err)
			}
			if v.(int) != i {
				t.FailNow()
			}
		} else {
			t.FailNow()
		}
	}
}

func TestSkipListIter_Seek(t *testing.T) {
	skipList := NewSkipList(comparator)
	for i := 0; i < 100; i++ {
		skipList.Insert(i)
	}
	iter := skipList.Iterator()
	err := iter.Seek(10)
	if err != nil {
		t.FailNow()
	}
	v, err := iter.At()
	if v.(int) != 10 {
		t.FailNow()
	}
	err = iter.Seek(101)
	if err == nil {
		t.FailNow()
	}
}
