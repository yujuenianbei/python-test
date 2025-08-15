// ppop11.ts - Person Popularity Optimizer v1.1
// This is a simple demonstration script for TS compilation and execution.

interface Person {
    name: string;
    age: number;
    popularity: number;
    incrementPopularity(): void;
}

class PersonImpl implements Person {
    name: string;
    age: number;
    popularity: number;

    constructor(name: string, age: number, popularity: number) {
        this.name = name;
        this.age = age;
        this.popularity = popularity;
    }

    incrementPopularity(): void {
        this.popularity += 1;
    }

    toString(): string {
        return `${this.name} (Age: ${this.age}, Popularity: ${this.popularity})`;
    }
}

// Example usage
const person1 = new PersonImpl("Alice", 30, 5);
const person2 = new PersonImpl("Bob", 25, 3);

console.log("Initial State:");
console.log(person1.toString());
console.log(person2.toString());

person1.incrementPopularity();
person2.incrementPopularity();
person2.incrementPopularity();

console.log("\nAfter incrementing popularity:");
console.log(person1.toString());
console.log(person2.toString());