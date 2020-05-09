package data_structure

import (
	"errors"
	"fmt"
	"math/rand"
	"time"
)

const (
	SkipListMaxLevel = 7
)

var (
	ErrNotFound   = errors.New("value not found")
	ErrOutOfRange = errors.New("out of range")
)

type SkipListComparator func(interface{}, interface{}) int

type RandomIntGenerator func() int

func defaultRandomIntGenerator() RandomIntGenerator {
	rand.Seed(time.Now().UnixNano())
	return rand.Int
}

type skipListNode struct {
	next  [SkipListMaxLevel]*skipListNode
	span  [SkipListMaxLevel]int // 每一层到下一个节点之间的跨度，也就是中间间隔的节点数
	value interface{}
	level int8
}

func (n *skipListNode) Next(level int) *skipListNode {
	return n.next[level]
}

func (n *skipListNode) SetNext(level int, next *skipListNode) *skipListNode {
	n.next[level] = next
	return n
}

func (n *skipListNode) Span(level int) int {
	return n.span[level]
}

func (n *skipListNode) SetSpan(level, span int) *skipListNode {
	n.span[level] = span
	return n
}

func (n *skipListNode) Value() interface{} {
	return n.value
}

type SkipList struct {
	head               *skipListNode
	comparator         SkipListComparator
	randomIntGenerator RandomIntGenerator
}

func NewSkipList(comparator SkipListComparator) *SkipList {
	return &SkipList{
		head:               &skipListNode{value: nil, level: SkipListMaxLevel - 1},
		comparator:         comparator,
		randomIntGenerator: defaultRandomIntGenerator(),
	}
}

// 我们需要知道每一层的最后一个小于当前值的节点
func (s *SkipList) findLastLessNode(v interface{}) [SkipListMaxLevel]*skipListNode {
	nodes := [SkipListMaxLevel]*skipListNode{}
	node := s.head
	level := node.level
	for level >= 0 {
		if node.next[level] != nil && s.comparator(node.next[level].value, v) < 0 {
			node = node.next[level]
		} else {
			nodes[level] = node
			level--
		}
	}
	return nodes
}

// 1/4的概率上涨一层
func (s *SkipList) newSkipListNode(v interface{}) *skipListNode {
	level := int8(0)
	for s.randomIntGenerator()%4 == 0 && level != SkipListMaxLevel-1 {
		level += 1
	}
	return &skipListNode{
		next:  [7]*skipListNode{},
		value: v,
		level: level,
	}
}

func (s *SkipList) getSpan(x, y *skipListNode) int {
	if x == y {
		return 0
	}
	level := x.level
	span := 0
	for level >= 0 {
		if x.next[level] == y {
			span += x.span[level]
			break
		}
		// next如果是null，代表无穷大
		if x.next[level] != nil && s.comparator(x.next[level].value, y.value) <= 0 {
			span += x.span[level]
			x = x.next[level]
		} else {
			level--
		}
	}
	return span
}

func (s *SkipList) Insert(v interface{}) error {
	lastNodes := s.findLastLessNode(v)
	node := s.newSkipListNode(v)
	for i := int8(0); i < SkipListMaxLevel; i++ {
		if i <= node.level {
			nextNode := lastNodes[i].next[i]
			lastNode := lastNodes[i]
			node.next[i] = nextNode
			lastNode.next[i] = node

			// 第一层的节点span赋值很简单，举例肯定是非0即1，lastNode的肯定是1，因为这个节点会插入在lastNode后面
			// 当前节点的span不确定，要看lastNode之前的span，等于是node代替了lastNode
			if i == 0 {
				node.span[i] = lastNode.span[i]
				lastNode.span[i] = 1
			} else {
				// 上一层 lastNode到node节点的span已经算出来了，本次只需要算当前层的lastNode到上一层的lastNode的span
				// 然后加起来即可
				newLastNodeSpan := s.getSpan(lastNode, lastNodes[i-1]) + lastNodes[i-1].span[i-1]
				node.span[i] = lastNode.span[i] - newLastNodeSpan + 1
				lastNode.span[i] = newLastNodeSpan
			}
		} else {
			lastNodes[i].span[i] += 1
		}
	}
	return nil
}

func (s *SkipList) compare(node *skipListNode, v interface{}) int {
	if node == s.head {
		return -1
	}
	if node == nil {
		return 1
	}
	return s.comparator(node.Value(), v)
}

func (s *SkipList) Delete(v interface{}) bool {
	lastNodes := s.findLastLessNode(v)
	level0LastNode := lastNodes[0]
	if s.compare(level0LastNode.Next(0), v) != 0 {
		return false
	}

	for level := 0; level < SkipListMaxLevel; level++ {
		lastNode := lastNodes[level]
		nextNode := lastNode.Next(level)
		if s.compare(nextNode, v) == 0 {
			lastNode.SetNext(level, nextNode.Next(level))
			lastNode.SetSpan(level, lastNode.Span(level)-1+nextNode.Span(level))
		} else {
			lastNode.SetSpan(level, lastNode.Span(level)-1)
		}
	}
	return true
}

func (s *SkipList) Print() {
	colWidth := []int{}
	for node := s.head.next[0]; node != nil; node = node.next[0] {
		s := fmt.Sprintf("%d", node.value)
		colWidth = append(colWidth, len(s))
	}
	sep := "-"
	for level := SkipListMaxLevel - 1; level >= 0; level-- {
		node := s.head
		span := 0
		for node != nil {
			if node == s.head {
				fmt.Printf("*")
			} else {
				fmt.Printf("%v", node.value)
			}
			for i := 0; i < 2*node.span[level]-1; i++ {
				if i%2 == 0 {
					fmt.Printf(sep)
				} else {
					w := colWidth[(i-1)/2+span]
					for j := 0; j < w; j++ {
						fmt.Printf(sep)
					}
				}
			}
			if node.next[level] == nil && node.span[level] != 0 {
				w := colWidth[len(colWidth)-1]
				for j := 0; j < w; j++ {
					fmt.Printf(sep)
				}
			}
			span += node.span[level]
			node = node.next[level]
		}
		fmt.Printf("*\n")
	}
}

func (s *SkipList) Iterator() Iterator {
	return newSkipListIter(s)
}

type Iterator interface {
	Next() bool
	At() (interface{}, error)
	Seek(interface{}) error
}

type skipListIter struct {
	s       *SkipList
	curNode *skipListNode
}

func newSkipListIter(s *SkipList) *skipListIter {
	return &skipListIter{s: s, curNode: s.head}
}

func (s *skipListIter) Next() bool {
	if s.curNode == nil {
		return false
	}
	s.curNode = s.curNode.Next(0)
	return s.curNode != nil
}

func (s *skipListIter) At() (interface{}, error) {
	if s.curNode == nil {
		return nil, ErrOutOfRange
	}
	return s.curNode.Value(), nil
}

func (s *skipListIter) Seek(v interface{}) error {
	lastNodes := s.s.findLastLessNode(v)
	firstGteNode := lastNodes[0].Next(0) // 第一个大于等于的节点
	if firstGteNode == nil || s.s.comparator(v, firstGteNode.Value()) != 0 {
		s.curNode = nil
		return ErrNotFound
	}
	s.curNode = firstGteNode
	return nil
}
