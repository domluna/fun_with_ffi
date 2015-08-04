package main

import "C"
import (
        "math/rand"
)

func simulatePi(needles int) float64 {
        hits := 0

        for i := 0; i < needles; i++ {
                x, y := rand.Float64(), rand.Float64()
                if x*x + y*y <= 1.0 {
                        hits += 1
                }
        }

        return 4.0 * float64(hits) / float64(needles)
}

//export EstimatePi
func EstimatePi(sims, needles int) float64 {
        ch := make(chan float64, 1)

        // Could also use sync.WaitGroup here but the timings
        // didn't make a difference.
        for i := 0; i < sims; i++ {
                go func() {
                        val := simulatePi(needles)
                        ch <- val
                }()
        }

        est := 0.0
        for i := 0; i < sims; i++ {
                est += <-ch
        }
        close(ch)

        return est / float64(sims)
}

func main() {}
