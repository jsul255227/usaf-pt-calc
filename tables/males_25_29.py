# males_25_29.py
# Official USAF PT scoring tables for Males 25-29
# Template based on males_under_25.py. Fill in each component as official values are provided.

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
MALE_25_29_RUN = [
    (0, mmss_to_seconds('9:22'), 60.0),
    (mmss_to_seconds('9:23'), mmss_to_seconds('9:45'), 59.5),
    (mmss_to_seconds('9:46'), mmss_to_seconds('9:58'), 59.0),
    (mmss_to_seconds('9:59'), mmss_to_seconds('10:10'), 58.5),
    (mmss_to_seconds('10:11'), mmss_to_seconds('10:23'), 58.0),
    (mmss_to_seconds('10:24'), mmss_to_seconds('10:37'), 57.5),
    (mmss_to_seconds('10:38'), mmss_to_seconds('10:51'), 57.0),
    (mmss_to_seconds('10:52'), mmss_to_seconds('11:06'), 56.5),
    (mmss_to_seconds('11:07'), mmss_to_seconds('11:22'), 56.0),
    (mmss_to_seconds('11:23'), mmss_to_seconds('11:38'), 55.5),
    (mmss_to_seconds('11:39'), mmss_to_seconds('11:56'), 55.0),
    (mmss_to_seconds('11:57'), mmss_to_seconds('12:14'), 54.5),
    (mmss_to_seconds('12:15'), mmss_to_seconds('12:33'), 54.0),
    (mmss_to_seconds('12:34'), mmss_to_seconds('12:53'), 53.5),
    (mmss_to_seconds('12:54'), mmss_to_seconds('13:14'), 52.0),
    (mmss_to_seconds('13:15'), mmss_to_seconds('13:36'), 50.5),
    (mmss_to_seconds('13:37'), mmss_to_seconds('14:00'), 49.0),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 46.5),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 44.0),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 41.0),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 38.0),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 35.0), # 16:22*
]

# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
# Example: (101, float('inf'), 60.0) means 101 or more shuttles earns 60.0 points.
MALE_25_29_HAMR = [
    (98, float('inf'), 60.0),      # > 97
    (92, 96, 59.5),
    (88, 91, 59.0),
    (86, 87, 58.5),
    (83, 85, 58.0),
    (80, 82, 57.5),
    (77, 79, 57.0),
    (74, 76, 56.5),
    (71, 73, 56.0),
    (68, 70, 55.5),
    (65, 67, 55.0),
    (62, 64, 54.5),
    (59, 61, 54.0),
    (56, 58, 53.5),
    (54, 55, 52.0),
    (51, 53, 50.5),
    (48, 50, 49.0),
    (45, 47, 46.5),
    (42, 44, 44.0),
    (39, 41, 41.0),
    (36, 38, 38.0),
    (33, 35, 35.0),                # 33*-35
]

# ----------------------
# Upper Body: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (67, float('inf'), 20.0) means 67 or more push-ups earns 20.0 points.
MALE_25_29_PUSHUPS = [
    (63, float('inf'), 20.0),      # > 62
    (61, 62, 19.7),
    (60, 60, 19.4),
    (59, 59, 19.0),
    (58, 58, 18.8),
    (57, 57, 18.6),
    (56, 56, 18.4),
    (55, 55, 18.2),
    (54, 54, 18.0),
    (53, 53, 17.8),
    (52, 52, 17.6),
    (51, 51, 17.5),
    (50, 50, 17.4),
    (49, 49, 17.2),
    (48, 48, 17.0),
    (47, 47, 16.8),
    (46, 46, 16.6),
    (45, 45, 16.2),
    (44, 44, 16.0),
    (43, 43, 15.6),
    (42, 42, 15.4),
    (41, 41, 15.0),
    (40, 40, 14.6),
    (39, 39, 14.4),
    (38, 38, 14.0),
    (37, 37, 13.6),
    (36, 36, 13.0),
    (35, 35, 12.6),
    (34, 34, 12.0),
    (33, 33, 11.6),
    (32, 32, 11.0),
    (31, 31, 10.6),
    (30, 30, 10.0),
    (29, 29, 7.0),
    (28, 28, 4.0),
    (27, 27, 1.0),                # 27*
]

# ----------------------
# Upper Body: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (41, float('inf'), 20.0) means 41 or more HR push-ups earns 20.0 points.
MALE_25_29_HR_PUSHUPS = [
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
MALE_25_29_SITUPS = [
    (57, float('inf'), 20.0),      # > 56
    (55, 56, 19.5),
    (54, 54, 19.0),
    (53, 53, 18.8),
    (52, 52, 18.4),
    (51, 51, 18.0),
    (50, 50, 17.6),
    (49, 49, 17.4),
    (48, 48, 17.0),
    (47, 47, 16.6),
    (46, 46, 16.0),
    (45, 45, 15.0),
    (44, 44, 14.0),
    (43, 43, 13.0),
    (42, 42, 12.6),
    (41, 41, 12.0),
    (40, 40, 9.0),
    (39, 39, 6.0),
    (38, 38, 3.0),                # 38*
]

# ----------------------
# Core: 2 min Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Example: (50, float('inf'), 20.0) means 50 or more crunches earns 20.0 points.
MALE_25_29_CRUNCH = [
    (49, float('inf'), 20.0),      # > 48
    (47, 48, 19.6),
    (46, 46, 19.3),
    (45, 45, 18.9),
    (44, 44, 18.6),
    (43, 43, 18.2),
    (42, 42, 17.9),
    (41, 41, 17.5),
    (40, 40, 17.1),
    (39, 39, 16.8),
    (38, 38, 16.4),
    (37, 37, 16.1),
    (36, 36, 15.7),
    (35, 35, 15.4),
    (34, 34, 15.0),
    (33, 33, 14.6),
    (32, 32, 14.3),
    (31, 31, 13.9),
    (30, 30, 13.6),
    (29, 29, 13.2),
    (28, 28, 12.9),
    (27, 27, 12.5),
    (26, 26, 12.1),
    (25, 25, 11.8),
    (24, 24, 11.4),
    (23, 23, 11.1),
    (22, 22, 10.7),
    (21, 21, 10.4),
    (20, 20, 10.0),                # 20*
]

# ----------------------
# Core: Forearm Plank
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Longer time = higher score.
# Example: (0, mmss_to_seconds('3:30'), 20.0) means any time from 0 up to 3:30 earns 20.0 points.
MALE_25_29_PLANK = [
    (mmss_to_seconds('3:31'), float('inf'), 20.0),      # > 3:30
    (mmss_to_seconds('3:25'), mmss_to_seconds('3:30'), 19.7),
    (mmss_to_seconds('3:20'), mmss_to_seconds('3:24'), 19.3),
    (mmss_to_seconds('3:14'), mmss_to_seconds('3:19'), 18.9),
    (mmss_to_seconds('3:03'), mmss_to_seconds('3:13'), 18.2),
    (mmss_to_seconds('3:00'), mmss_to_seconds('3:02'), 18.0),
    (mmss_to_seconds('2:40'), mmss_to_seconds('2:59'), 16.7),
    (mmss_to_seconds('2:20'), mmss_to_seconds('2:39'), 15.3),
    (mmss_to_seconds('2:00'), mmss_to_seconds('2:19'), 14.0),
    (mmss_to_seconds('1:40'), mmss_to_seconds('1:59'), 12.7),
    (mmss_to_seconds('1:20'), mmss_to_seconds('1:39'), 11.3),
    (mmss_to_seconds('1:00'), mmss_to_seconds('1:19'), 10.0), # 1:00*
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
# * Minimum Component Values (Males 25-29):
#   - Run time < [FILL IN]
#   - 20 m HAMR Shuttles > [FILL IN]
#
# Composite Score Categories:
#   - Excellent:     ≥ 90.0 pts
#   - Satisfactory:  75.0 - 89.9
#   - Unsatisfactory: < 75.0
#
# These notes apply to all scoring tables and should be referenced in calculator logic and UI.
