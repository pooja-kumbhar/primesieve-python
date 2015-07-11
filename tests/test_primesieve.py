import primesieve

def test_count_primes():
    assert primesieve.count_primes(100) == 25
    assert primesieve.count_primes(10**6) == 78498
    assert primesieve.count_primes(100, 10**6) == 78473

def test_parallel_count_primes():
    assert primesieve.parallel_count_primes(10**10) == 455052511
    assert primesieve.parallel_count_primes(10**9, 10**10) == 404204977

def test_nth_prime():
    assert primesieve.nth_prime(25) == 97
    assert primesieve.nth_prime(26) == 101
    assert primesieve.nth_prime(1, 100) == 101
    assert primesieve.nth_prime(100, 1000000) == 1001311

def test_parallel_nth_prime():
    assert primesieve.parallel_nth_prime(10**8) == 2038074743

def test_generate_primes():
    assert primesieve.generate_primes(10) == [2,3,5,7]
    assert primesieve.generate_primes(10, 20) == [11,13,17,19]

def test_generate_n_primes():
    assert primesieve.generate_n_primes(7) == [2,3,5,7,11,13,17]
    assert primesieve.generate_n_primes(5, 100) == [101,103,107,109,113]

def test_iterator():
    it = primesieve.Iterator()
    assert it.next_prime() == 2
    assert it.next_prime() == 3
    assert it.next_prime() == 5
    assert it.next_prime() == 7
    assert it.next_prime() == 11
    assert it.previous_prime() == 7
    assert it.next_prime() == 11
