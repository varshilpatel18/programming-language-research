"""
visualizer.py
Creates a clean pie chart for a categorical column
Fixes label overlap by:
- grouping small categories into "Other"
- using legend outside chart instead of labels on slices
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import logging
from collections import Counter
import os

logger = logging.getLogger(__name__)

def create_pie_chart_from_rows(
    rows,
    column_name: str,
    output_path="piechart.png",
    title=None,
    min_percent=3  # any category <3% goes into "Other"
):
    try:
        values = [row[column_name] for row in rows if row[column_name] not in (None, "", " ")]
        counts = Counter(values)

        if not counts:
            raise ValueError("No valid categorical data found for pie chart.")

        total = sum(counts.values())

        # Group small categories into "Other"
        main_counts = {}
        other_count = 0
        for label, count in counts.items():
            percent = (count / total) * 100
            if percent < min_percent:
                other_count += count
            else:
                main_counts[label] = count

        if other_count > 0:
            main_counts["Other"] = other_count

        labels = list(main_counts.keys())
        sizes = list(main_counts.values())

        # Bigger figure for clarity
        fig, ax = plt.subplots(figsize=(9, 7))

        # Pie chart WITHOUT labels (legend handles labels)
        wedges, texts, autotexts = ax.pie(
            sizes,
            autopct="%1.1f%%",
            startangle=90,
            pctdistance=0.75
        )

        ax.axis("equal")

        if title:
            ax.set_title(title, fontsize=14)

        # Legend outside chart
        ax.legend(
            wedges,
            labels,
            title=column_name,
            loc="center left",
            bbox_to_anchor=(1, 0.5),
            fontsize=9
        )

        plt.tight_layout()
        plt.savefig(output_path, bbox_inches="tight")
        plt.close(fig)

        logger.info("Pie chart saved to %s", output_path)
        return os.path.abspath(output_path)

    except Exception:
        logger.exception("Failed to create pie chart for column %s", column_name)
        raise
