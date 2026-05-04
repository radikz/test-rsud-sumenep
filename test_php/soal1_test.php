<?php
use PHPUnit\Framework\TestCase;

require_once dirname(__DIR__) . '/php/soal1/soal1.php';
class Soal1_test extends TestCase
{
    public function testExamples1() {
        $this->assertSame(17, maxTriSum([3,2,6,8,2,3]));
    }
    public function testExamples2() {
        $this->assertSame(18, maxTriSum([2,1,8,0,6,4,8,6,2,4]));
    }
    public function testExamples3() {
        $this->assertSame(41, maxTriSum([-7,12,-7,29,-5,0,-7,0,0,29]));
    }

    public function testEdgeCases1() {
        $this->assertSame(6, maxTriSum([1,1,1,2,2,3]));     
    }
    public function testEdgeCases2() {         
        $this->assertSame(-6, maxTriSum([-5,-4,-3,-2,-1]));      
    }
    public function testEdgeCases3() {   
        $this->assertSame(0, maxTriSum([0,0,0,1,-1]));          
    }
    public function testEdgeCases4() {      
        $this->assertSame(10, maxTriSum([10,10,10,10,10]));      
    }
    public function testEdgeCases5() {   
        $this->assertSame(40, maxTriSum([10,10,10,10,30]));     
    }
}
