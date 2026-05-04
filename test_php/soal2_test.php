<?php

use PHPUnit\Framework\TestCase;

require_once dirname(__DIR__) . '/php/soal2/soal2.php';
class Soal2_test extends TestCase
{
    public function testExamples1()
    {
        $this->assertSame(7, sumTwoSmallestNumbers([19, 5, 42, 2, 77]));
    }
    public function testExamples2()
    {
        $this->assertSame(3453455, sumTwoSmallestNumbers([10, 343445353, 3453445, 3453545353453]));
    }
    public function testExamples3()
    {
        $this->assertSame(4, sumTwoSmallestNumbers([4, 1, 7, 3]));
    }

    public function testEdgeCases1()
    {
        $this->assertSame(13, sumTwoSmallestNumbers([5, 8, 12, 19, 22]));
    }
    public function testEdgeCases2()
    {
        $this->assertSame(6, sumTwoSmallestNumbers([15, 28, 4, 2, 43]));
    }
    public function testEdgeCases3()
    {
        $this->assertSame(10, sumTwoSmallestNumbers([3, 87, 45, 12, 7]));
    }
}
