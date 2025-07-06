# males_over_60.py
# Official USAF PT scoring tables for Males Over 60
# Template based on previous age groups. Fill in each component as official values are provided.

# Helper function: Convert 'mm:ss' string to total seconds (int)
def mmss_to_seconds(mmss):
    """
    Convert a time string in 'mm:ss' format to total seconds.
    Example: '9:13' -> 553
    """
    m, s = map(int, mmss.split(':'))
    return m * 60 + s

# ----------------------
# Cardio: 1.5 Mile Run (official July 2025)
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Lower time = higher score.
# Updated to match official USAF PT table (July 2025)
MALE_OVER_60_RUN = [
    (0, mmss_to_seconds('11:22') - 1, 60.0),                 # < 11:22
    (mmss_to_seconds('11:22'), mmss_to_seconds('11:56'), 59.5),
    (mmss_to_seconds('11:57'), mmss_to_seconds('12:14'), 59.0),
    (mmss_to_seconds('12:15'), mmss_to_seconds('12:33'), 58.5),
    (mmss_to_seconds('12:34'), mmss_to_seconds('12:53'), 58.0),
    (mmss_to_seconds('12:54'), mmss_to_seconds('13:14'), 57.5),
    (mmss_to_seconds('13:15'), mmss_to_seconds('13:36'), 57.0),
    (mmss_to_seconds('13:37'), mmss_to_seconds('14:00'), 56.5),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 56.0),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 55.5),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 55.0),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 54.5),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 54.0),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 52.5),
    (mmss_to_seconds('16:58'), mmss_to_seconds('17:34'), 51.0),
    (mmss_to_seconds('17:35'), mmss_to_seconds('18:14'), 49.5),
    (mmss_to_seconds('18:15'), mmss_to_seconds('18:56'), 47.0),
    (mmss_to_seconds('18:57'), mmss_to_seconds('19:43'), 44.5),
    (mmss_to_seconds('19:44'), mmss_to_seconds('20:33'), 41.5),
    (mmss_to_seconds('20:34'), mmss_to_seconds('21:28'), 38.5),
    (mmss_to_seconds('21:29'), mmss_to_seconds('22:28'), 35.0), # 22:28*
]

# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
# Updated to match official USAF PT table (July 2025)
MALE_OVER_60_HAMR = [
    (72, float('inf'), 60.0),         # > 71
    (65, 70, 59.5),
    (62, 64, 59.0),
    (59, 61, 58.5),
    (56, 58, 58.0),
    (54, 55, 57.5),
    (51, 53, 57.0),
    (48, 50, 56.5),
    (45, 47, 56.0),
    (42, 44, 55.5),
    (39, 41, 55.0),
    (36, 38, 54.5),
    (33, 35, 54.0),
    (30, 32, 52.5),
    (27, 29, 51.0),
    (24, 26, 49.5),
    (22, 23, 47.0),
    (19, 21, 44.5),
    (16, 18, 41.5),
    (13, 15, 38.5),
    (10, 12, 35.0),                   # 10*-12
]

# ----------------------
# Strength: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Updated to match official USAF PT table (July 2025)
MALE_OVER_60_PUSHUPS = [
    (31, float('inf'), 20.0),      # > 30
    (29, 30, 19.5),
    (28, 28, 19.0),
    (27, 27, 18.6),
    (26, 26, 18.0),
    (25, 25, 17.6),
    (24, 24, 17.0),
    (23, 23, 16.0),
    (22, 22, 15.0),
    (21, 21, 14.0),
    (20, 20, 13.0),
    (19, 19, 12.6),
    (18, 18, 12.0),
    (17, 17, 11.6),
    (16, 16, 11.0),
    (15, 15, 10.6),
    (14, 14, 10.0),
    (13, 13, 7.0),
    (12, 12, 4.0),
    (11, 11, 1.0),                # 11*
]

# ----------------------
# Strength: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Updated to match official USAF PT table (July 2025)
MALE_OVER_60_HR_PUSHUPS = [
    (31, float('inf'), 20.0),      # > 30
    (29, 30, 19.5),
    (28, 28, 19.0),
    (27, 27, 18.5),
    (26, 26, 18.0),
    (25, 25, 17.5),
    (24, 24, 17.0),
    (23, 23, 16.5),
    (22, 22, 16.0),
    (21, 21, 15.5),
    (20, 20, 15.0),
    (19, 19, 14.5),
    (18, 18, 14.0),
    (17, 17, 13.5),
    (16, 16, 13.0),
    (15, 15, 12.5),
    (14, 14, 12.0),
    (13, 13, 11.5),
    (12, 12, 11.0),
    (11, 11, 10.5),
    (10, 10, 10.0),                # 10*
]

# ----------------------
# Strength: 1 min Sit-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Updated to match official USAF PT table (July 2025)
MALE_OVER_60_SITUPS = [
    (42, float('inf'), 20.0),      # ≥ 42
    (41, 41, 19.7),
    (40, 40, 19.4),
    (39, 39, 19.0),
    (38, 38, 18.8),
    (37, 37, 18.4),
    (36, 36, 18.2),
    (35, 35, 18.0),
    (34, 34, 17.8),
    (33, 33, 17.6),
    (32, 32, 17.2),
    (31, 31, 17.0),
    (30, 30, 16.0),
    (29, 29, 15.6),
    (28, 28, 15.0),
    (27, 27, 14.6),
    (26, 26, 14.0),
    (25, 25, 13.6),
    (24, 24, 13.0),
    (23, 23, 12.6),
    (22, 22, 12.0),
    (21, 21, 9.0),
    (20, 20, 6.0),
    (19, 19, 3.0),                # 19*
]

# ----------------------
# Core: 2 min Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Updated to match official USAF PT table (July 2025)
MALE_OVER_60_CRUNCH = [
    (36, float('inf'), 20.0),      # > 35
    (34, 35, 19.6),
    (33, 33, 19.3),
    (32, 32, 18.9),
    (31, 31, 18.6),
    (30, 30, 18.2),
    (29, 29, 17.9),
    (28, 28, 17.5),
    (27, 27, 17.1),
    (26, 26, 16.8),
    (25, 25, 16.4),
    (24, 24, 16.1),
    (23, 23, 15.7),
    (22, 22, 15.4),
    (21, 21, 15.0),
    (20, 20, 14.6),
    (19, 19, 14.3),
    (18, 18, 13.9),
    (17, 17, 13.6),
    (16, 16, 13.2),
    (15, 15, 12.9),
    (14, 14, 12.5),
    (13, 13, 12.1),
    (12, 12, 11.8),
    (11, 11, 11.4),
    (10, 10, 11.1),
    (9, 9, 10.7),
    (8, 8, 10.4),
    (7, 7, 10.0),                # 7*
]

# ----------------------
# Core: Forearm Plank
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
# Updated to match official USAF PT table (July 2025)
MALE_OVER_60_PLANK = [
    (mmss_to_seconds('2:56'), float('inf'), 20.0),   # > 2:55
    (mmss_to_seconds('2:50'), mmss_to_seconds('2:55'), 19.7),
    (mmss_to_seconds('2:45'), mmss_to_seconds('2:49'), 19.3),
    (mmss_to_seconds('2:39'), mmss_to_seconds('2:44'), 18.9),
    (mmss_to_seconds('2:32'), mmss_to_seconds('2:38'), 18.5),
    (mmss_to_seconds('2:25'), mmss_to_seconds('2:31'), 18.0),
    (mmss_to_seconds('2:05'), mmss_to_seconds('2:24'), 16.7),
    (mmss_to_seconds('1:55'), mmss_to_seconds('2:04'), 16.0),
    (mmss_to_seconds('1:25'), mmss_to_seconds('1:54'), 14.0),
    (mmss_to_seconds('1:05'), mmss_to_seconds('1:24'), 12.7),
    (mmss_to_seconds('0:45'), mmss_to_seconds('1:04'), 11.3),
    (mmss_to_seconds('0:25'), mmss_to_seconds('0:44'), 10.0),   # 0:25* minimum
]

# ----------------------
# Add additional component tables below as official values are provided.
# ----------------------
