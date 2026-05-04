<?php

use PHPUnit\Framework\TestCase;

require_once dirname(__DIR__) . '/php/soal3/soal3.php';
class Soal3_test extends TestCase
{
    public function testExamples1()
    {
        $expected3 = [[7, 8, 9], [6, 5, 4], [1, 2, 3]];
        $this->assertSame($expected3, generateSnakePattern(3));
    }
    public function testExamples2()
    {
        $expected2 = [[4, 3], [1, 2]];
        $this->assertSame($expected2, generateSnakePattern(2));
    }
    
}
