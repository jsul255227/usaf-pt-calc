# males_30_34.py
# Official USAF PT scoring tables for Males 30-34
# Template based on males_under_25.py and males_25_29.py. Fill in each component as official values are provided.

# Helper function: Convert 'mm:ss' string to total seconds (int)
def mmss_to_seconds(mmss):
    """
    Convert a time string in 'mm:ss' format to total seconds.
    Example: '9:13' -> 553
    """
    m, s = map(int, mmss.split(':'))
    return m * 60 + s

# ----------------------
# Cardio: 1.5 Mile Run
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Lower time = higher score.
# Example: (0, mmss_to_seconds('9:12'), 60.0) means any time from 0 up to 9:12 earns 60.0 points.
MALE_30_34_RUN = [
    (mmss_to_seconds('9:35'), mmss_to_seconds('9:58'), 59.5),
    (mmss_to_seconds('9:59'), mmss_to_seconds('10:10'), 59.0),
    (mmss_to_seconds('10:11'), mmss_to_seconds('10:23'), 58.5),
    (mmss_to_seconds('10:24'), mmss_to_seconds('10:37'), 58.0),
    (mmss_to_seconds('10:38'), mmss_to_seconds('10:51'), 57.5),
    (mmss_to_seconds('10:52'), mmss_to_seconds('11:06'), 57.0),
    (mmss_to_seconds('11:07'), mmss_to_seconds('11:22'), 56.5),
    (mmss_to_seconds('11:23'), mmss_to_seconds('11:38'), 56.0),
    (mmss_to_seconds('11:39'), mmss_to_seconds('11:56'), 55.5),
    (mmss_to_seconds('11:57'), mmss_to_seconds('12:14'), 55.0),
    (mmss_to_seconds('12:15'), mmss_to_seconds('12:33'), 54.5),
    (mmss_to_seconds('12:34'), mmss_to_seconds('12:53'), 54.0),
    (mmss_to_seconds('12:54'), mmss_to_seconds('13:14'), 53.5),
    (mmss_to_seconds('13:15'), mmss_to_seconds('13:36'), 52.0),
    (mmss_to_seconds('13:37'), mmss_to_seconds('14:00'), 50.5),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 48.0),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 45.5),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 43.0),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 40.5),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 38.0),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 35.0), # 16:57*
]

# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
# Example: (101, float('inf'), 60.0) means 101 or more shuttles earns 60.0 points.
MALE_30_34_HAMR = [
    (95, float('inf'), 60.0),      # > 94
    (88, 93, 59.5),
    (86, 87, 59.0),
    (83, 85, 58.5),
    (80, 82, 58.0),
    (77, 79, 57.5),
    (74, 76, 57.0),
    (71, 73, 56.5),
    (68, 70, 56.0),
    (65, 67, 55.5),
    (62, 64, 55.0),
    (59, 61, 54.5),
    (56, 58, 54.0),
    (54, 55, 53.5),
    (51, 53, 52.0),
    (48, 50, 50.5),
    (45, 47, 48.0),
    (42, 44, 45.5),
    (39, 41, 43.0),
    (36, 38, 40.5),
    (33, 35, 38.0),
    (30, 32, 35.0),                # 30*-32
]

# ----------------------
# Upper Body: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (67, float('inf'), 20.0) means 67 or more push-ups earns 20.0 points.
MALE_30_34_PUSHUPS = [
    (58, float('inf'), 20.0),      # > 57
    (56, 57, 19.8),
    (55, 55, 19.6),
    (54, 54, 19.4),
    (53, 53, 19.2),
    (52, 52, 19.0),
    (51, 51, 18.8),
    (50, 50, 18.6),
    (49, 49, 18.5),
    (48, 48, 18.4),
    (47, 47, 18.2),
    (46, 46, 18.0),
    (45, 45, 17.8),
    (44, 44, 17.6),
    (43, 43, 17.4),
    (42, 42, 17.2),
    (41, 41, 17.0),
    (40, 40, 16.6),
    (39, 39, 16.0),
    (38, 38, 15.6),
    (37, 37, 15.4),
    (36, 36, 15.0),
    (35, 35, 14.6),
    (34, 34, 14.0),
    (33, 33, 13.6),
    (32, 32, 13.4),
    (31, 31, 13.0),
    (30, 30, 12.0),
    (29, 29, 11.0),
    (28, 28, 10.6),
    (27, 27, 10.0),
    (26, 26, 7.0),
    (25, 25, 4.0),
    (24, 24, 1.0),                # 24*
]

# ----------------------
# Upper Body: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (41, float('inf'), 20.0) means 41 or more HR push-ups earns 20.0 points.
MALE_30_34_HR_PUSHUPS = [
    (41, float('inf'), 20.0),      # > 40
    (39, 40, 19.6),
    (38, 38, 19.2),
    (37, 37, 18.8),
    (36, 36, 18.4),
    (35, 35, 18.0),
    (34, 34, 17.6),
    (33, 33, 17.2),
    (32, 32, 16.8),
    (31, 31, 16.4),
    (30, 30, 16.0),
    (29, 29, 15.6),
    (28, 28, 15.2),
    (27, 27, 14.8),
    (26, 26, 14.4),
    (25, 25, 14.0),
    (24, 24, 13.6),
    (23, 23, 13.2),
    (22, 22, 12.8),
    (21, 21, 12.4),
    (20, 20, 12.0),
    (19, 19, 11.6),
    (18, 18, 11.2),
    (17, 17, 10.8),
    (16, 16, 10.4),
    (15, 15, 10.0),                # 15*
]

# ----------------------
# Core: 1 min Sit-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (58, float('inf'), 20.0) means 58 or more sit-ups earns 20.0 points.
MALE_30_34_SITUPS = [
    (55, float('inf'), 20.0),      # > 54
    (53, 54, 19.7),
    (52, 52, 19.4),
    (51, 51, 19.0),
    (50, 50, 18.8),
    (49, 49, 18.4),
    (48, 48, 18.0),
    (47, 47, 17.6),
    (46, 46, 17.4),
    (45, 45, 17.0),
    (44, 44, 16.6),
    (43, 43, 16.0),
    (42, 42, 15.0),
    (41, 41, 14.0),
    (40, 40, 13.0),
    (39, 39, 12.0),
    (38, 38, 9.0),
    (37, 37, 6.0),
    (36, 36, 3.0),                # 36*
]

# ----------------------
# Core: 2 min Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (50, float('inf'), 20.0) means 50 or more crunches earns 20.0 points.
MALE_30_34_CRUNCH = [
    (48, float('inf'), 20.0),      # > 47
    (46, 47, 19.6),
    (45, 45, 19.3),
    (44, 44, 18.9),
    (43, 43, 18.6),
    (42, 42, 18.2),
    (41, 41, 17.9),
    (40, 40, 17.5),
    (39, 39, 17.1),
    (38, 38, 16.8),
    (37, 37, 16.4),
    (36, 36, 16.1),
    (35, 35, 15.7),
    (34, 34, 15.4),
    (33, 33, 15.0),
    (32, 32, 14.6),
    (31, 31, 14.3),
    (30, 30, 13.9),
    (29, 29, 13.6),
    (28, 28, 13.2),
    (27, 27, 12.9),
    (26, 26, 12.5),
    (25, 25, 12.1),
    (24, 24, 11.8),
    (23, 23, 11.4),
    (22, 22, 11.1),
    (21, 21, 10.7),
    (20, 20, 10.4),
    (19, 19, 10.0),                # 19*
]

# ----------------------
# Core: Forearm Plank
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
# Example: (mmss_to_seconds('3:36'), float('inf'), 20.0) means any time above 3:35 earns 20.0 points.
MALE_30_34_PLANK = [
    # Official USAF PT Plank scoring table for Males 30-34
    # Each tuple: (start_seconds, end_seconds, score)
    # Ranges are inclusive. Higher time = higher score.
    # (mmss_to_seconds('3:26'), float('inf'), 20.0) means any time above 3:25 earns 20.0 points.
    (mmss_to_seconds('3:26'), float('inf'), 20.0),   # > 3:25
    (mmss_to_seconds('3:20'), mmss_to_seconds('3:25'), 19.7),
    (mmss_to_seconds('3:15'), mmss_to_seconds('3:19'), 19.3),
    (mmss_to_seconds('3:09'), mmss_to_seconds('3:14'), 18.9),
    (mmss_to_seconds('3:02'), mmss_to_seconds('3:08'), 18.5),
    (mmss_to_seconds('2:55'), mmss_to_seconds('3:01'), 18.0),
    (mmss_to_seconds('2:35'), mmss_to_seconds('2:54'), 16.7),
    (mmss_to_seconds('2:15'), mmss_to_seconds('2:34'), 15.3),
    (mmss_to_seconds('1:55'), mmss_to_seconds('2:14'), 14.0),
    (mmss_to_seconds('1:35'), mmss_to_seconds('1:54'), 12.7),
    (mmss_to_seconds('1:15'), mmss_to_seconds('1:34'), 11.3),
    (mmss_to_seconds('0:55'), mmss_to_seconds('1:14'), 10.0),   # 0:55* minimum
]

# ----------------------
# USAF PT Test: Scoring Notes and Composite Categories
# ----------------------
# Health Risk Category:
#   - low, moderate or high risk for: current and future cardiovascular disease, diabetes, certain cancers, and other health problems.
#
# Passing Requirements:
#   1) Achieve a composite point total ≥ 75 points
#   2) Meet minimum point values for all components
#
# * Minimum Component Values (Males 30-34):
#   - Run time < [FILL IN]
#   - 20 m HAMR Shuttles > [FILL IN]
#
# Composite Score Categories:
#   - Excellent:     ≥ 90.0 pts
#   - Satisfactory:  75.0 - 89.9
#   - Unsatisfactory: < 75.0
#
# These notes apply to all scoring tables and should be referenced in calculator logic and UI.
