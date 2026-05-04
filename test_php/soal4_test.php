<?php

use PHPUnit\Framework\TestCase;

require_once dirname(__DIR__) . '/php/soal4/soal4.php';
class Soal4_Test extends TestCase
{
    public function testExamples() {
        $this->assertSame("############5616", maskify("4556364607935616"));
    }
    public function testExamples2() {
        $this->assertSame("#######5616", maskify("64607935616"));
    }
    public function testExamples3() {
        $this->assertSame("1", maskify("1"));
    }
    public function testExamples4() {
        $this->assertSame("", maskify(""));
    }
    public function testExamples5() {
        $this->assertSame("##ippy", maskify("Skippy"));
    }
    public function testExamples6() {
        $this->assertSame("####################################man!", maskify("Nananananananananananananananana Batman!"));
    }

    public function testAdditional() {
        $this->assertSame("######7890", maskify("1234567890"));
    }
    public function testAdditional2() {
        $this->assertSame("abcd", maskify("abcd"));
    }
    public function testAdditional3() {
        $this->assertSame("a", maskify("a"));
    }
    public function testAdditional4() {
        $this->assertSame("123", maskify("123"));
    }
}
