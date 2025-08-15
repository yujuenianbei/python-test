/**
 * PPOP - Person Popularity Optimization Program
 * A TypeScript implementation for calculating and optimizing person popularity scores
 */

// Interface for a Person object
interface Person {
  id: number;
  name: string;
  followers: number;
  engagementRate: number;
  popularityScore?: number;
}

// Class to handle popularity calculations
class PopularityOptimizer {
  private readonly engagementWeight: number = 0.7;
  private readonly followerWeight: number = 0.3;

  /**
   * Calculate popularity score based on followers and engagement
   * @param person The person object to calculate score for
   * @returns The calculated popularity score
   */
  public calculatePopularity(person: Person): number {
    // Simple weighted score calculation
    const score = (
      person.followers * this.followerWeight + 
      person.engagementRate * 1000 * this.engagementWeight
    );
    
    return Math.round(score);
  }

  /**
   * Update popularity scores for an array of people
   * @param people Array of Person objects
   * @returns Array of Person objects with updated popularity scores
   */
  public updateAllPopularity(people: Person[]): Person[] {
    return people.map(person => {
      return {
        ...person,
        popularityScore: this.calculatePopularity(person)
      };
    });
  }

  /**
   * Find the most popular person in an array
   * @param people Array of Person objects
   * @returns The Person with the highest popularity score
   */
  public findMostPopular(people: Person[]): Person | undefined {
    const peopleWithScores = this.updateAllPopularity(people);
    return peopleWithScores.reduce((prev, current) => {
      return (prev.popularityScore || 0) > (current.popularityScore || 0) ? prev : current;
    });
  }
}

// Sample data
const people: Person[] = [
  { id: 1, name: "Alice", followers: 1500, engagementRate: 0.85 },
  { id: 2, name: "Bob", followers: 2300, engagementRate: 0.67 },
  { id: 3, name: "Charlie", followers: 800, engagementRate: 0.92 }
];

// Main execution
const optimizer = new PopularityOptimizer();
const peopleWithScores = optimizer.updateAllPopularity(people);
const mostPopular = optimizer.findMostPopular(people);

console.log("People with Popularity Scores:");
peopleWithScores.forEach(person => {
  console.log(`${person.name}: ${person.popularityScore}`);
});

console.log("\nMost Popular Person:");
if (mostPopular) {
  console.log(`${mostPopular.name} with a score of ${mostPopular.popularityScore}`);
}

// Export for use in other modules
export { Person, PopularityOptimizer };