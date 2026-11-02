import (
    "strconv"
)

func countSeniors(details []string) int {
    count := 0
    for _, detail:= range details{
        age, _ := strconv.ParseInt(detail[11:13], 10, 32)
        if age>60{
            count += 1
        }
    }
    return count
}