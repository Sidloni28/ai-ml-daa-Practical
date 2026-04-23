def job_sequencing(jobs):
    # Sort jobs based on profit (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find maximum deadline to determine the number of slots
    max_deadline = max(job[1] for job in jobs)

    # Create slots
    slots = [None] * max_deadline
    total_profit = 0
    step_count = 0

    for job in jobs:
        job_id, deadline, profit = job
        
        # Try to place job in latest possible slot
        for i in range(deadline - 1, -1, -1):
            step_count += 1
            if slots[i] is None:
                slots[i] = job_id
                total_profit += profit
                break

    scheduled_jobs = [job for job in slots if job is not None]

    return scheduled_jobs, total_profit, step_count


# 🔹 Taking input from the user
jobs = []
n = int(input("Enter number of jobs: "))

for i in range(n):
    print(f"\nEnter details for Job {i+1}")
    job_id = input("Job ID: ")
    deadline = int(input("Deadline: "))
    profit = int(input("Profit: "))
    
    jobs.append((job_id, deadline, profit))


scheduled, profit, steps = job_sequencing(jobs)

print("\nScheduled Jobs:", scheduled)
print("Total Profit:", profit)
print("Step Count:", steps)
