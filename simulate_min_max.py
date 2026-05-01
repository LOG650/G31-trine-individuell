import math
import random
from collections import defaultdict

PRODUCTS = {
    "Maskara": (3, 5),
    "Dagkrem": (2, 4),
    "Håndkrem": (2, 4),
    "Parfyme": (1, 3),
    "Eyeliner": (1, 3),
    "Leppestift": (2, 4),
    "Leppepomade": (3, 5),
}

VARIANTS = {
    "Baseline": PRODUCTS,
    "Variant A": {name: (minv + 1, maxv + 1) for name, (minv, maxv) in PRODUCTS.items()},
    "Variant B": {name: (minv + 2, maxv + 2) for name, (minv, maxv) in PRODUCTS.items()},
    "Variant A_half": {name: (minv + 0.5, maxv + 0.5) for name, (minv, maxv) in PRODUCTS.items()},
    "Variant A_onehalf": {name: (minv + 1.5, maxv + 1.5) for name, (minv, maxv) in PRODUCTS.items()},
}

DAYS = 90
ORDER_MULTIPLE = 3


def poisson(lam: float) -> int:
    x = 0
    p = math.exp(-lam)
    prod = 1.0
    while prod > p:
        prod *= random.random()
        x += 1
    return x - 1


def demand_for_day() -> dict:
    result = {}
    for product in PRODUCTS:
        if random.random() < 0.2:
            lam = 8.0
        else:
            lam = 3.0
        result[product] = max(0, poisson(lam))
    return result


def lead_time_days() -> int:
    # Realistisk lead time 1-3 dager, ofte 2-3
    r = random.random()
    if r < 0.15:
        return 1
    if r < 0.8:
        return 2
    return 3


def adjust_for_tuesday(arrival_day: int) -> int:
    # 0=Monday, 1=Tuesday, ..., 6=Sunday
    if arrival_day % 7 == 1:
        return arrival_day + 1
    return arrival_day


def next_multiple_of_3(value: int) -> int:
    return ((value + ORDER_MULTIPLE - 1) // ORDER_MULTIPLE) * ORDER_MULTIPLE


def simulate(variant_name: str, variant: dict, daily_demands: list, days: int = DAYS) -> dict:
    inventory = {name: maxv for name, (_, maxv) in variant.items()}
    pending_orders = []
    metrics = {
        "total_days": 0,
        "tom_hylle_events": defaultdict(int),
        "lav_hylle_events": defaultdict(int),
        "lost_demand": defaultdict(int),
        "total_demand": defaultdict(int),
        "avg_binding": defaultdict(float),
    }

    for day in range(days):
        # Receive any pending orders for today
        arrivals = [order for order in pending_orders if order[0] == day]
        for _, product, qty in arrivals:
            inventory[product] += qty
        pending_orders = [order for order in pending_orders if order[0] != day]

        demand = daily_demands[day]
        metrics["total_days"] += 1

        for product, amount in demand.items():
            minv, maxv = variant[product]
            current = inventory[product]
            metrics["total_demand"][product] += amount
            if current == 0:
                metrics["tom_hylle_events"][product] += 1
            if current < 2:
                metrics["lav_hylle_events"][product] += 1

            served = min(current, amount)
            lost = amount - served
            inventory[product] -= served
            metrics["lost_demand"][product] += lost
            metrics["avg_binding"][product] += inventory[product]

            if inventory[product] <= minv:
                order_qty = next_multiple_of_3(maxv - inventory[product])
                if order_qty > 0:
                    arrival = day + lead_time_days()
                    arrival = adjust_for_tuesday(arrival)
                    pending_orders.append((arrival, product, order_qty))

    for product in PRODUCTS:
        metrics["avg_binding"][product] /= days
    return metrics


def generate_demand_series(days: int = DAYS) -> list:
    return [demand_for_day() for _ in range(days)]


def summarize(metrics: dict) -> dict:
    days = metrics["total_days"]
    summary = {}
    for product in PRODUCTS:
        summary[product] = {
            "tom_hylle_rate": metrics["tom_hylle_events"][product] / days * 100,
            "lav_hylle_rate": metrics["lav_hylle_events"][product] / days * 100,
            "avg_binding": metrics["avg_binding"][product],
            "lost_demand": metrics["lost_demand"][product],
            "total_demand": metrics["total_demand"][product],
        }
    summary["total_lost_demand"] = sum(metrics["lost_demand"].values())
    summary["total_demand"] = sum(metrics["total_demand"].values())
    return summary


def print_report(results: dict):
    header = ["Produkt", "Tom%", "Lav%", "Bind", "Tapt", "Etterspørsel"]
    print("; ".join(header))
    for product in PRODUCTS:
        row = results[product]
        print(
            f"{product}; {row['tom_hylle_rate']:.1f}; {row['lav_hylle_rate']:.1f}; "
            f"{row['avg_binding']:.1f}; {row['lost_demand']}; {row['total_demand']}"
        )


def run():
    random.seed(0)
    daily_demands = generate_demand_series(DAYS)
    all_summaries = {}
    for name, variant in VARIANTS.items():
        metrics = simulate(name, variant, daily_demands)
        summary = summarize(metrics)
        all_summaries[name] = summary

    for name, summary in all_summaries.items():
        print(f"\n=== {name} ===")
        print_report(summary)
        total_lost = summary["total_lost_demand"]
        total_demand = summary["total_demand"]
        print(f"Totalt tapt etterspørsel: {total_lost} av {total_demand} ({total_lost/total_demand*100:.1f}%)")

if __name__ == "__main__":
    run()
