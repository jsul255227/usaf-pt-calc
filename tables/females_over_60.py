# females_over_60.py
# Official USAF PT scoring tables for Females Age 60+
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

# Cardio: 1.5 Mile Run
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Lower time = higher score.
FEMALE_OVER_60_RUN = [
    (0, mmss_to_seconds('14:00') - 1, 60.0),                 # < 14:00
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:52'), 59.5),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 59.0),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 58.5),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 58.0),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 57.5),
    (mmss_to_seconds('16:58'), mmss_to_seconds('17:34'), 57.0),
    (mmss_to_seconds('17:35'), mmss_to_seconds('18:14'), 56.5),
    (mmss_to_seconds('18:15'), mmss_to_seconds('18:56'), 56.0),
    (mmss_to_seconds('18:57'), mmss_to_seconds('19:43'), 55.5),
    (mmss_to_seconds('19:44'), mmss_to_seconds('20:33'), 54.0),
    (mmss_to_seconds('20:34'), mmss_to_seconds('21:28'), 52.5),
    (mmss_to_seconds('21:29'), mmss_to_seconds('22:28'), 51.0),
    (mmss_to_seconds('22:29'), mmss_to_seconds('23:34'), 47.0),
    (mmss_to_seconds('23:35'), mmss_to_seconds('24:46'), 43.0),
    (mmss_to_seconds('24:47'), mmss_to_seconds('26:06'), 39.0),
    (mmss_to_seconds('26:07'), mmss_to_seconds('27:27'), 35.0), # 27:27*
]
# ----------------------

# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
FEMALE_OVER_60_HAMR = [
    (49, float('inf'), 60.0),         # > 48
    (42, 48, 59.5),
    (39, 41, 59.0),
    (36, 38, 58.5),
    (33, 35, 58.0),
    (30, 32, 57.5),
    (27, 29, 57.0),
    (24, 26, 56.5),
    (22, 23, 56.0),
    (19, 21, 55.5),
    (16, 18, 54.0),
    (13, 15, 52.5),
    (10, 12, 51.0),
    (7, 9, 47.0),
    (5, 6, 43.0),
    (2, 4, 39.0),
    (1, 1, 35.0),                  # 1*
    (0, 0, 35.0),                  # 0 (for completeness, below minimum)
]
# ----------------------

# Strength: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_OVER_60_PUSHUPS = [
    (22, float('inf'), 20.0),      # > 21
    (20, 21, 19.5),
    (19, 19, 19.0),
    (18, 18, 18.8),
    (17, 17, 18.0),
    (16, 16, 17.6),
    (15, 15, 17.0),
    (14, 14, 16.0),
    (13, 13, 15.0),
    (12, 12, 14.0),
    (11, 11, 13.0),
    (10, 10, 12.0),
    (9, 9, 11.4),
    (8, 8, 10.6),
    (7, 7, 10.0),
    (6, 6, 7.0),
    (5, 5, 4.0),
    (4, 4, 1.0),                # 4*
]
# ----------------------

# Strength: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_OVER_60_HR_PUSHUPS = [
    (25, float('inf'), 20.0),      # > 24
    (23, 24, 19.6),
    (22, 22, 19.2),
    (21, 21, 18.8),
    (20, 20, 18.4),
    (19, 19, 18.0),
    (18, 18, 17.6),
    (17, 17, 17.2),
    (16, 16, 16.8),
    (15, 15, 16.4),
    (14, 14, 16.0),
    (13, 13, 15.6),
    (12, 12, 15.2),
    (11, 11, 14.8),
    (10, 10, 14.4),
    (9, 9, 14.0),
    (8, 8, 13.6),
    (7, 7, 13.2),
    (6, 6, 12.8),
    (5, 5, 12.4),
    (4, 4, 12.0),
    (3, 3, 11.6),
    (2, 2, 11.2),
    (1, 1, 10.0),                # 1*
]
# ----------------------

# Strength: 1 min Sit-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_OVER_60_SITUPS = [
    (32, float('inf'), 20.0),      # > 31
    (30, 31, 19.7),
    (29, 29, 19.4),
    (28, 28, 19.0),
    (27, 27, 18.8),
    (26, 26, 18.0),
    (25, 25, 17.8),
    (24, 24, 17.6),
    (23, 23, 17.4),
    (22, 22, 17.2),
    (21, 21, 17.0),
    (20, 20, 16.8),
    (19, 19, 16.6),
    (18, 18, 16.4),
    (17, 17, 16.0),
    (16, 16, 15.6),
    (15, 15, 15.0),
    (14, 14, 14.6),
    (13, 13, 14.0),
    (12, 12, 13.0),
    (11, 11, 12.0),
    (10, 10, 9.0),
    (9, 9, 6.0),
    (8, 8, 3.0),                # 8*
]
# ----------------------

# Strength: 2 min Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_OVER_60_CRUNCH = [
    (33, float('inf'), 20.0),      # > 32
    (31, 32, 19.6),
    (30, 30, 19.3),
    (29, 29, 18.9),
    (28, 28, 18.5),
    (27, 27, 18.1),
    (26, 26, 17.8),
    (25, 25, 17.4),
    (24, 24, 17.0),
    (23, 23, 16.7),
    (22, 22, 16.3),
    (21, 21, 15.9),
    (20, 20, 15.6),
    (19, 19, 15.2),
    (18, 18, 14.8),
    (17, 17, 14.4),
    (16, 16, 14.1),
    (15, 15, 13.7),
    (14, 14, 13.3),
    (13, 13, 13.0),
    (12, 12, 12.6),
    (11, 11, 12.2),
    (10, 10, 11.9),
    (9, 9, 11.5),
    (8, 8, 11.1),
    (7, 7, 10.7),
    (6, 6, 10.4),
    (5, 5, 10.0),                # 5*
]
# ----------------------

# Core: Forearm Plank
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
FEMALE_OVER_60_PLANK = [
    (mmss_to_seconds('2:51'), float('inf'), 20.0),      # > 2:50
    (mmss_to_seconds('2:45'), mmss_to_seconds('2:50'), 19.7),
    (mmss_to_seconds('2:39'), mmss_to_seconds('2:44'), 19.3),
    (mmss_to_seconds('2:32'), mmss_to_seconds('2:38'), 18.8),
    (mmss_to_seconds('2:25'), mmss_to_seconds('2:31'), 18.4),
    (mmss_to_seconds('2:05'), mmss_to_seconds('2:24'), 17.1),
    (mmss_to_seconds('1:45'), mmss_to_seconds('2:04'), 15.8),
    (mmss_to_seconds('1:25'), mmss_to_seconds('1:44'), 14.5),
    (mmss_to_seconds('1:05'), mmss_to_seconds('1:24'), 13.2),
    (mmss_to_seconds('0:30'), mmss_to_seconds('1:04'), 11.0),
    (mmss_to_seconds('0:25'), mmss_to_seconds('0:29'), 10.6),
    (mmss_to_seconds('0:20'), mmss_to_seconds('0:24'), 10.3),
    (mmss_to_seconds('0:15'), mmss_to_seconds('0:19'), 10.0),   # 0:15*
]
# ----------------------
# Add additional component tables below as official values are provided.
# ----------------------
