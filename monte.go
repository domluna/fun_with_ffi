package main

import (
        "math/rand"
        "fmt"
        "runtime"
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

func estimatePi(sims, needles int) float64 {
        fmt.Printf("Running %d simulations with %d needles being dropped\n", sims, needles)
        ch := make(chan float64, 1)

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

func main() {
        fmt.Println(estimatePi(1000, 10000))
}
