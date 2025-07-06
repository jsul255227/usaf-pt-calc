# females_55_59.py
# Official USAF PT scoring tables for Females Age 55-59
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
FEMALE_55_59_RUN = [
    (0, mmss_to_seconds('13:14') - 1, 60.0),                 # < 13:14
    (mmss_to_seconds('13:15'), mmss_to_seconds('14:00'), 59.5),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 59.0),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 58.5),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 58.0),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 57.5),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 57.0),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 56.5),
    (mmss_to_seconds('16:58'), mmss_to_seconds('17:34'), 56.0),
    (mmss_to_seconds('17:35'), mmss_to_seconds('18:14'), 55.5),
    (mmss_to_seconds('18:15'), mmss_to_seconds('18:56'), 55.0),
    (mmss_to_seconds('18:57'), mmss_to_seconds('19:43'), 53.5),
    (mmss_to_seconds('19:44'), mmss_to_seconds('20:33'), 52.0),
    (mmss_to_seconds('20:34'), mmss_to_seconds('21:28'), 49.0),
    (mmss_to_seconds('21:29'), mmss_to_seconds('22:28'), 46.0),
    (mmss_to_seconds('22:29'), mmss_to_seconds('23:34'), 43.0),
    (mmss_to_seconds('23:35'), mmss_to_seconds('24:46'), 39.0),
    (mmss_to_seconds('24:47'), mmss_to_seconds('26:06'), 35.0), # 26:06*
]
# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
FEMALE_55_59_HAMR = [
    (55, float('inf'), 60.0),         # > 54
    (48, 54, 59.5),
    (45, 47, 59.0),
    (42, 44, 58.5),
    (39, 41, 58.0),
    (36, 38, 57.5),
    (33, 35, 57.0),
    (30, 32, 56.5),
    (27, 29, 56.0),
    (24, 26, 55.5),
    (22, 23, 55.0),
    (19, 21, 53.5),
    (16, 18, 52.0),
    (13, 15, 49.0),
    (10, 12, 46.0),
    (7, 9, 43.0),
    (5, 6, 39.0),
    (2, 4, 35.0),                  # 2*-4
    (0, 1, 35.0),                  # 0-1 (for completeness, below minimum)
]
# ----------------------
# Strength: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_55_59_PUSHUPS = [
    (29, float('inf'), 20.0),      # > 28
    (27, 28, 19.7),
    (26, 26, 19.4),
    (25, 25, 19.2),
    (24, 24, 19.0),
    (23, 23, 18.6),
    (22, 22, 18.0),
    (21, 21, 17.6),
    (20, 20, 17.2),
    (19, 19, 17.0),
    (18, 18, 16.8),
    (17, 17, 16.6),
    (16, 16, 16.4),
    (15, 15, 16.2),
    (14, 14, 16.0),
    (13, 13, 15.0),
    (12, 12, 14.0),
    (11, 11, 13.0),
    (10, 10, 12.0),
    (9, 9, 11.0),
    (8, 8, 10.0),
    (7, 7, 7.0),
    (6, 6, 4.0),
    (5, 5, 1.0),                # 5*
]
# ----------------------
# Strength: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_55_59_HR_PUSHUPS = [
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
FEMALE_55_59_SITUPS = [
    (33, float('inf'), 20.0),      # > 32
    (31, 32, 19.7),
    (30, 30, 19.4),
    (29, 29, 19.2),
    (28, 28, 19.0),
    (27, 27, 18.0),
    (26, 26, 17.8),
    (25, 25, 17.6),
    (24, 24, 17.2),
    (23, 23, 17.0),
    (22, 22, 16.0),
    (21, 21, 15.0),
    (20, 20, 14.6),
    (19, 19, 14.0),
    (18, 18, 13.6),
    (17, 17, 13.0),
    (16, 16, 12.6),
    (15, 15, 12.0),
    (14, 14, 9.0),
    (13, 13, 6.0),
    (12, 12, 3.0),                # 12*
]
# ----------------------
# Strength: 2 min Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_55_59_CRUNCH = [
    (39, float('inf'), 20.0),      # > 38
    (37, 38, 19.7),
    (36, 36, 19.4),
    (35, 35, 19.1),
    (34, 34, 18.8),
    (33, 33, 18.4),
    (32, 32, 18.1),
    (31, 31, 17.8),
    (30, 30, 17.5),
    (29, 29, 17.2),
    (28, 28, 16.9),
    (27, 27, 16.6),
    (26, 26, 16.3),
    (25, 25, 15.9),
    (24, 24, 15.6),
    (23, 23, 15.3),
    (22, 22, 15.0),
    (21, 21, 14.7),
    (20, 20, 14.4),
    (19, 19, 14.1),
    (18, 18, 13.8),
    (17, 17, 13.4),
    (16, 16, 13.1),
    (15, 15, 12.8),
    (14, 14, 12.5),
    (13, 13, 12.2),
    (12, 12, 11.9),
    (11, 11, 11.6),
    (10, 10, 11.3),
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
FEMALE_55_59_PLANK = [
    (mmss_to_seconds('2:56'), float('inf'), 20.0),      # > 2:55
    (mmss_to_seconds('2:50'), mmss_to_seconds('2:55'), 19.7),
    (mmss_to_seconds('2:44'), mmss_to_seconds('2:49'), 19.3),
    (mmss_to_seconds('2:37'), mmss_to_seconds('2:43'), 18.8),
    (mmss_to_seconds('2:30'), mmss_to_seconds('2:36'), 18.4),
    (mmss_to_seconds('2:10'), mmss_to_seconds('2:29'), 17.1),
    (mmss_to_seconds('1:50'), mmss_to_seconds('2:09'), 15.8),
    (mmss_to_seconds('1:30'), mmss_to_seconds('1:49'), 14.5),
    (mmss_to_seconds('1:10'), mmss_to_seconds('1:29'), 13.2),
    (mmss_to_seconds('0:50'), mmss_to_seconds('1:09'), 11.9),
    (mmss_to_seconds('0:30'), mmss_to_seconds('0:49'), 10.6),
    (mmss_to_seconds('0:25'), mmss_to_seconds('0:29'), 10.3),
    (mmss_to_seconds('0:20'), mmss_to_seconds('0:24'), 10.0),   # 0:20*
]
# ----------------------
# Add additional component tables below as official values are provided.
# ----------------------
