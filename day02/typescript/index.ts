import fs from "fs"


function part1() {
    const data = String(fs.readFileSync("./input.txt"))
    const lines = data.split("\n")

    let sum = 0
    for (const line of lines) {
        const [gameInfo, gameRecord] = line.split(":")
        const [_, gameIdStr] = gameInfo.split(" ")
        const gameId = parseInt(gameIdStr)
        const gameSets = gameRecord.split(";")
        let validLine = true

        for (const gameSet of gameSets) {
            const moves = gameSet.split(",")

            for (const move of moves) {
                const [_, numStr, color] = move.split(" ")
                const num = parseInt(numStr)

                if (color === "red" && num > 12) {
                    validLine = false
                } else if (color === "green" && num > 13) {
                    validLine = false
                } else if (color === "blue" && num > 14) {
                    validLine = false
                }
            }
        }
        if (validLine) {
            sum += gameId
        }
    }
    console.log(sum)
}

function part2() {
    const data = String(fs.readFileSync("./input.txt"))
    const lines = data.split("\n")

    let sum = 0
    for (const line of lines) {
        const [_, gameRecord] = line.split(":")
        const gameSets = gameRecord.split(";")

        const reds: number[] = []
        const blues: number[] = []
        const greens: number[] = []

        for (const gameSet of gameSets) {
            const moves = gameSet.split(",")

            for (const move of moves) {
                const [_, numStr, color] = move.split(" ")
                const num = parseInt(numStr)

                if (color === "red") {
                    reds.push(num)
                } else if (color === "green") {
                    greens.push(num)
                } else if (color === "blue") {
                    blues.push(num)
                }
            }
        }
        sum += Math.max(...reds) * Math.max(...greens) * Math.max(...blues)
    }
    console.log(sum)
}

part1()
part2()
