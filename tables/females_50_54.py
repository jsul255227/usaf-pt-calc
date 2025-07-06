# females_50_54.py
# Official USAF PT scoring tables for Females Age 50-54
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
# Add component tables below as official values are provided.
# ----------------------

# ----------------------
# Cardio: 1.5 Mile Run
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Lower time = higher score.
FEMALE_50_54_RUN = [
    (0, mmss_to_seconds('12:53') - 1, 60.0),                 # < 12:53
    (mmss_to_seconds('12:54'), mmss_to_seconds('13:36'), 59.5),
    (mmss_to_seconds('13:37'), mmss_to_seconds('14:00'), 59.0),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 58.5),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 58.0),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 57.5),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 57.0),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 56.5),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 56.0),
    (mmss_to_seconds('16:58'), mmss_to_seconds('17:34'), 55.5),
    (mmss_to_seconds('17:35'), mmss_to_seconds('18:14'), 55.0),
    (mmss_to_seconds('18:15'), mmss_to_seconds('18:56'), 53.5),
    (mmss_to_seconds('18:57'), mmss_to_seconds('19:43'), 52.0),
    (mmss_to_seconds('19:44'), mmss_to_seconds('20:33'), 49.5),
    (mmss_to_seconds('20:34'), mmss_to_seconds('21:28'), 46.0),
    (mmss_to_seconds('21:29'), mmss_to_seconds('22:28'), 42.5),
    (mmss_to_seconds('22:29'), mmss_to_seconds('23:34'), 39.0),
    (mmss_to_seconds('23:35'), mmss_to_seconds('24:46'), 35.0), # 24:46*
]
# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
FEMALE_50_54_HAMR = [
    (57, float('inf'), 60.0),         # > 56
    (51, 56, 59.5),
    (48, 50, 59.0),
    (45, 47, 58.5),
    (42, 44, 58.0),
    (39, 41, 57.5),
    (36, 38, 57.0),
    (33, 35, 56.5),
    (30, 32, 56.0),
    (27, 29, 55.5),
    (24, 26, 55.0),
    (22, 23, 53.5),
    (19, 21, 52.0),
    (16, 18, 49.5),
    (13, 15, 46.0),
    (10, 12, 42.5),
    (5, 9, 39.0),                  # 5*-9
    (0, 4, 35.0),                  # 0-4 (for completeness, below minimum)
]
# ----------------------
# Strength: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_50_54_PUSHUPS = [
    (36, float('inf'), 20.0),      # > 35
    (34, 35, 19.8),
    (33, 33, 19.6),
    (32, 32, 19.4),
    (31, 31, 19.2),
    (30, 30, 19.0),
    (29, 29, 18.8),
    (28, 28, 18.6),
    (27, 27, 18.4),
    (26, 26, 18.2),
    (25, 25, 18.0),
    (24, 24, 17.6),
    (23, 23, 17.4),
    (22, 22, 17.3),
    (21, 21, 17.2),
    (20, 20, 17.0),
    (19, 19, 16.8),
    (18, 18, 16.6),
    (17, 17, 16.4),
    (16, 16, 16.2),
    (15, 15, 16.0),
    (14, 14, 15.0),
    (13, 13, 14.0),
    (12, 12, 13.0),
    (11, 11, 12.0),
    (10, 10, 11.0),
    (9, 9, 10.0),
    (8, 8, 7.0),
    (7, 7, 4.0),
    (6, 6, 1.0),                # 6*
]
# ----------------------
# Strength: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_50_54_HR_PUSHUPS = [
    (26, float('inf'), 20.0),      # > 25
    (24, 25, 19.6),
    (23, 23, 19.2),
    (22, 22, 18.8),
    (21, 21, 18.4),
    (20, 20, 18.0),
    (19, 19, 17.6),
    (18, 18, 17.2),
    (17, 17, 16.8),
    (16, 16, 16.4),
    (15, 15, 16.0),
    (14, 14, 15.6),
    (13, 13, 15.2),
    (12, 12, 14.8),
    (11, 11, 14.4),
    (10, 10, 14.0),
    (9, 9, 13.6),
    (8, 8, 13.2),
    (7, 7, 12.8),
    (6, 6, 12.4),
    (5, 5, 12.0),
    (4, 4, 11.6),
    (3, 3, 11.2),
    (2, 2, 10.8),
    (1, 1, 10.0),                # 1*
]
# ----------------------
# Strength: 1 min Sit-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_50_54_SITUPS = [
    (33, float('inf'), 20.0),      # > 32
    (31, 32, 19.5),
    (30, 30, 19.0),
    (29, 29, 18.0),
    (28, 28, 17.8),
    (27, 27, 17.6),
    (26, 26, 17.2),
    (25, 25, 17.0),
    (24, 24, 16.0),
    (23, 23, 15.0),
    (22, 22, 14.0),
    (21, 21, 13.0),
    (20, 20, 12.0),
    (19, 19, 9.0),
    (18, 18, 6.0),
    (17, 17, 3.0),                # 17*
]
# ----------------------
# Strength: 2 min Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_50_54_CRUNCH = [
    (40, float('inf'), 20.0),      # > 39
    (38, 39, 19.7),
    (37, 37, 19.4),
    (36, 36, 19.1),
    (35, 35, 18.8),
    (34, 34, 18.5),
    (33, 33, 18.2),
    (32, 32, 17.9),
    (31, 31, 17.6),
    (30, 30, 17.3),
    (29, 29, 17.0),
    (28, 28, 16.7),
    (27, 27, 16.4),
    (26, 26, 16.1),
    (25, 25, 15.8),
    (24, 24, 15.5),
    (23, 23, 15.2),
    (22, 22, 14.8),
    (21, 21, 14.5),
    (20, 20, 14.2),
    (19, 19, 13.9),
    (18, 18, 13.6),
    (17, 17, 13.3),
    (16, 16, 13.0),
    (15, 15, 12.7),
    (14, 14, 12.4),
    (13, 13, 12.1),
    (12, 12, 11.8),
    (11, 11, 11.5),
    (10, 10, 11.2),
    (9, 9, 10.9),
    (8, 8, 10.6),
    (7, 7, 10.3),
    (6, 6, 10.0),                # 6*
]
# ----------------------
# Forearm Plank (seconds)
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
FEMALE_50_54_PLANK = [
    (mmss_to_seconds('3:01'), float('inf'), 20.0),      # > 3:00
    (mmss_to_seconds('2:55'), mmss_to_seconds('3:00'), 19.7),
    (mmss_to_seconds('2:49'), mmss_to_seconds('2:54'), 19.3),
    (mmss_to_seconds('2:42'), mmss_to_seconds('2:48'), 18.8),
    (mmss_to_seconds('2:35'), mmss_to_seconds('2:41'), 18.4),
    (mmss_to_seconds('2:15'), mmss_to_seconds('2:34'), 17.1),
    (mmss_to_seconds('1:55'), mmss_to_seconds('2:14'), 15.8),
    (mmss_to_seconds('1:35'), mmss_to_seconds('1:54'), 14.5),
    (mmss_to_seconds('1:15'), mmss_to_seconds('1:34'), 13.2),
    (mmss_to_seconds('0:55'), mmss_to_seconds('1:14'), 11.9),
    (mmss_to_seconds('0:35'), mmss_to_seconds('0:54'), 10.6),
    (mmss_to_seconds('0:30'), mmss_to_seconds('0:34'), 10.3),
    (mmss_to_seconds('0:25'), mmss_to_seconds('0:29'), 10.0),   # 0:25*
]
# ----------------------
# Add additional component tables below as official values are provided.
# ----------------------
