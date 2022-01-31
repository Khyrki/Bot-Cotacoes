CREATE DATABASE IF NOT EXISTS smarttbot;

use smarttbot;
CREATE TABLE IF NOT EXISTS candle_1min(
candle_id   INT AUTO_INCREMENT PRIMARY KEY,
moeda       VARCHAR(20)     NOT NULL,
date_time   DATETIME        NOT NULL,
open        DECIMAL(16, 10) NOT NULL,
low         DECIMAL(16, 10) NOT NULL,
high        DECIMAL(16, 10) NOT NULL,
close       DECIMAL(16, 10) NOT NULL);

CREATE TABLE IF NOT EXISTS candle_5min(
candle_id   INT AUTO_INCREMENT PRIMARY KEY,
moeda       VARCHAR(20)     NOT NULL,
date_time   DATETIME        NOT NULL,
open        DECIMAL(16, 10) NOT NULL,
low         DECIMAL(16, 10) NOT NULL,
high        DECIMAL(16, 10) NOT NULL,
close       DECIMAL(16, 10) NOT NULL);

CREATE TABLE IF NOT EXISTS candle_10min(
candle_id   INT AUTO_INCREMENT PRIMARY KEY,
moeda       VARCHAR(20)     NOT NULL,
date_time   DATETIME        NOT NULL,
open        DECIMAL(16, 10) NOT NULL,
low         DECIMAL(16, 10) NOT NULL,
high        DECIMAL(16, 10) NOT NULL,
close       DECIMAL(16, 10) NOT NULL);
